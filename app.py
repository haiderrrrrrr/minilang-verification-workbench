# app.py  ───────────────────────────────────────────────────────────────────────
"""
MiniLang Workbench – single-file Flask back-end

Endpoints
---------
GET  /               → landing page (templates/home.html)
GET  /workbench      → workbench shell (templates/workbench.html)
GET  /verify         → verification UI    (templates/verify.html)
GET  /equiv          → equivalence UI     (templates/equiv.html)

POST /parse          → SSA + verification pipeline
POST /equiv-api      → equivalence checker

JSON contracts
--------------
/parse
  { "program": "<MiniLang code>", "unroll": <k:int> }

/equiv-api
  { "progA": "<MiniLang A>", "progB": "<MiniLang B>", "unroll": <k:int> }
"""

from flask import Flask, request, jsonify, render_template
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl
import networkx as nx
from z3 import Solver, Int, Distinct, sat, Not, BoolRef, And, Or

from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser

app = Flask(__name__, template_folder="templates")


# ───────────────────────────────────────────────────────────────────────────────
# 1. ANTLR helpers
# ───────────────────────────────────────────────────────────────────────────────
class RecordingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
    def syntaxError(self, recognizer, symbol, line, column, msg, e):
        self.errors.append(f"line {line}:{column} {msg}")

def parse_program(text):
    stream = InputStream(text)
    lexer  = MiniLangLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniLangParser(tokens)
    listener = RecordingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    tree = parser.program()
    return tree, listener.errors


# ───────────────────────────────────────────────────────────────────────────────
# 2. Loop unrolling (for display)
# ───────────────────────────────────────────────────────────────────────────────
def unroll_loops(tree, k):
    out = []
    def walk(stmt):
        if stmt.forStatement():
            f = stmt.forStatement()
            init = f.assignmentExpression(0).getText() if f.assignmentExpression(0) else ""
            cond = f.expr().getText() if f.expr() else ""
            upd  = f.assignmentExpression(1).getText() if f.assignmentExpression(1) else ""
            out.append(f"for ({init}; {cond}; {upd}) {{")
            for _ in range(k):
                for b in f.block().statement(): walk(b)
            out.append("}")
        elif stmt.whileStatement():
            w = stmt.whileStatement()
            out.append(f"while ({w.expr().getText()}) "+"{")
            for _ in range(k):
                for b in w.block().statement(): walk(b)
            out.append("}")
        elif stmt.ifStatement():
            c = stmt.ifStatement()
            out.append(f"if ({c.expr().getText()}) "+"{")
            for b in c.block(0).statement(): walk(b)
            out.append("}")
            if c.block(1):
                out.append("else {")
                for b in c.block(1).statement(): walk(b)
                out.append("}")
        else:
            out.append(stmt.getText())
    for s in tree.statement(): walk(s)
    return "\n".join(out)


# ───────────────────────────────────────────────────────────────────────────────
# 3. Expression visitor → nested ('binop', None, L, op, R)
# ───────────────────────────────────────────────────────────────────────────────
def visit_expression(ctx):
    while ctx.getChildCount() == 1 and not isinstance(ctx.getChild(0), TerminalNodeImpl):
        ctx = ctx.getChild(0)
    if ctx.getChildCount() == 1 and isinstance(ctx.getChild(0), TerminalNodeImpl):
        txt = ctx.getText()
        return int(txt) if txt.isdigit() else txt
    if ctx.getChildCount() == 3 and ctx.getChild(0).getText()=="(" and ctx.getChild(2).getText()==")":
        return visit_expression(ctx.getChild(1))
    OPS = {"+","-","==","!=","<","<=",">",">="}
    expr, i = None, 0
    while i < ctx.getChildCount():
        tok = ctx.getChild(i).getText()
        if tok in OPS:
            right = visit_expression(ctx.getChild(i+1))
            expr = ("binop", None, expr, tok, right)
            i += 2
        else:
            sub = visit_expression(ctx.getChild(i))
            if expr is None:
                expr = sub
            i += 1
    return expr


# ───────────────────────────────────────────────────────────────────────────────
# 4. SSA generation  (pruned, array-aware)
# ───────────────────────────────────────────────────────────────────────────────
def generate_ssa(tree, unroll_k):
    ssa, ctrs, env = [], {}, {}
    def rename(e):
        if isinstance(e, tuple) and e[0]=="binop":
            _,_,L,op,R = e; return ("binop",None,rename(L),op,rename(R))
        if isinstance(e,str) and not e.isdigit():
            return env.get(e,e)
        return e
    def fresh(v):
        ctrs[v] = ctrs.get(v,0)+1
        name = f"{v}_{ctrs[v]}"
        env[v] = name
        return name
    def proc_assign(v,ctx):
        rhs = rename(visit_expression(ctx)); tgt = fresh(v)
        ssa.append(("assign",tgt,rhs))
    def proc_store(a,i,val):
        ssa.append(("store",a,rename(visit_expression(i)),rename(visit_expression(val))))
    def walk(stmt):
        if stmt.assignment():
            a = stmt.assignment()
            if a.arrayAccess():
                acc = a.arrayAccess()
                proc_store(acc.NAME().getText(),acc.expr(),a.expr())
            else:
                proc_assign(a.NAME().getText(),a.expr())
        elif stmt.assertStatement():
            a = stmt.assertStatement()
            ssa.append(("assert",fresh("assert"),rename(visit_expression(a.expr()))))
        elif stmt.ifStatement():
            c = stmt.ifStatement()
            for b in c.block(0).statement(): walk(b)
            if c.block(1):
                for b in c.block(1).statement(): walk(b)
        elif stmt.whileStatement():
            w = stmt.whileStatement()
            for _ in range(unroll_k):
                for b in w.block().statement(): walk(b)
        elif stmt.forStatement():
            f = stmt.forStatement()
            if f.assignmentExpression(0):
                ae = f.assignmentExpression(0)
                if ae.arrayAccess():
                    acc = ae.arrayAccess()
                    proc_store(acc.NAME().getText(),acc.expr(),ae.expr())
                else:
                    proc_assign(ae.NAME().getText(),ae.expr())
            for _ in range(unroll_k):
                for b in f.block().statement(): walk(b)
                if f.assignmentExpression(1):
                    ae = f.assignmentExpression(1)
                    if ae.arrayAccess():
                        acc = ae.arrayAccess()
                        proc_store(acc.NAME().getText(),acc.expr(),ae.expr())
                    else:
                        proc_assign(ae.NAME().getText(),ae.expr())
    for s in tree.statement(): walk(s)
    return ssa


# ───────────────────────────────────────────────────────────────────────────────
# 5. SSA optimisations
# ───────────────────────────────────────────────────────────────────────────────
def const_prop(ssa):
    consts,out = {},[]
    def fold(e):
        if isinstance(e,tuple) and e[0]=="binop":
            _,_,L,op,R=e; L2,R2=fold(L),fold(R)
            if isinstance(L2,int) and isinstance(R2,int):
                return eval(f"{L2}{op}{R2}")
            return ("binop",None,L2,op,R2)
        return consts.get(e,e)
    for inst in ssa:
        if inst[0]=="assign":
            _,v,rhs=inst; rhs2=fold(rhs)
            out.append(("assign",v,rhs2))
            if isinstance(rhs2,int): consts[v]=rhs2
        elif inst[0]=="assert":
            out.append(("assert",inst[1],fold(inst[2])))
        else:
            out.append(inst)
    return out

def cse(ssa):
    seen,out={},[]
    for inst in ssa:
        if inst[0]=="assign" and isinstance(inst[2],tuple):
            _,t,tpl=inst; _,_,L,op,R=tpl; key=(L,op,R)
            if key in seen:
                out.append(("assign",t,seen[key])); continue
            seen[key]=t
        out.append(inst)
    return out

def dead_code_elim(ssa):
    used,out=set(),[]
    def mark(e):
        if isinstance(e,tuple) and e[0]=="binop":
            mark(e[2]); mark(e[4])
        elif isinstance(e,str) and "_" in e:
            used.add(e)
    for inst in ssa:
        if inst[0]=="assert": mark(inst[2])
    for inst in ssa:
        if inst[0]=="assert" or inst[0]=="store" or inst[1] in used:
            out.append(inst)
    return out

def optimize_ssa(ssa):
    return dead_code_elim(cse(const_prop(ssa)))


# ───────────────────────────────────────────────────────────────────────────────
# 6. SMT-LIB generation
# ───────────────────────────────────────────────────────────────────────────────
def _expr_to_smt(e):
    if isinstance(e,int): return str(e)
    if isinstance(e,str): return e
    _,_,L,op,R=e
    m={"+":"+","-":"-","==":"=","!=":"distinct","<":"<","<=":"<=",">":">",">=":">="}
    return f"({m[op]} {_expr_to_smt(L)} {_expr_to_smt(R)})"

def generate_smt(ssa):
    decls,asts,seen=[],[],set()
    for inst in ssa:
        if inst[0]=="assign":
            _,v,r=inst
            if v not in seen:
                decls.append(f"(declare-const {v} Int)")
                seen.add(v)
            asts.append(f"(assert (= {v} {_expr_to_smt(r)}))")
        elif inst[0]=="assert":
            asts.append(f"(assert {_expr_to_smt(inst[2])})")
    return "\n".join(["(set-logic QF_LIA)"]+decls+asts+["(check-sat)","(get-model)"])


# ───────────────────────────────────────────────────────────────────────────────
# 7. Z3 verification
# ───────────────────────────────────────────────────────────────────────────────
def verify_ssa(ssa, max_cex=2):
    solver,vars_,post = Solver(),{},None
    def gv(n):
        if n not in vars_:
            vars_[n]=Int(n)
        return vars_[n]
    def e2z(e):
        if isinstance(e,int): return e
        if isinstance(e,str): return gv(e)
        _,_,L,op,R=e; Lz,Rz=e2z(L),e2z(R)
        return {"+":Lz+Rz,"-":Lz-Rz,"==":Lz==Rz,"!=":Lz!=Rz,
                "<":Lz<Rz,"<=":Lz<=Rz,">":Lz>Rz,">=":Lz>=Rz}[op]
    for inst in ssa:
        if inst[0]=="assign": solver.add(gv(inst[1])==e2z(inst[2]))
        elif inst[0]=="assert": post=e2z(inst[2])
    if post is None: return True,[{}]
    if not isinstance(post,BoolRef): post=post!=0
    solver.push(); solver.add(Not(post))
    cnt=[]
    while len(cnt)<max_cex and solver.check()==sat:
        m=solver.model()
        cnt.append({k:m[v].as_long() for k,v in vars_.items()})
        solver.add(Distinct(*vars_.values(),*[m[v] for v in vars_.values()]))
    solver.pop()
    if cnt: return False,cnt
    solver.push(); solver.add(post); w=[]
    if solver.check()==sat:
        m=solver.model(); w.append({k:m[v].as_long() for k,v in vars_.items()})
    solver.pop()
    return True,w


# ───────────────────────────────────────────────────────────────────────────────
# 8. CFG builder (for Cytoscape)
# ───────────────────────────────────────────────────────────────────────────────
def cfg_from_code(tree):
    G=nx.DiGraph(); m,ctr={},0
    def fresh():
        nonlocal ctr; ctr+=1; return f"S{ctr}"
    def label_all(b):
        for s in b.statement():
            m[s]=fresh()
            if s.ifStatement():
                c=s.ifStatement(); label_all(c.block(0))
                if c.block(1): label_all(c.block(1))
            elif s.whileStatement(): label_all(s.whileStatement().block())
            elif s.forStatement():   label_all(s.forStatement().block())
    label_all(tree)
    def build(stmts,succs):
        entries,exits=[],[]
        for s in stmts:
            nid=m[s]; G.add_node(nid,label=s.getText())
            if exits:
                for e in exits: G.add_edge(e,nid)
            else: entries.append(nid)
            exits=[nid]
            if s.ifStatement():
                c=s.ifStatement(); te,tx=build(c.block(0).statement(),succs)
                for e in te: G.add_edge(nid,e)
                if c.block(1):
                    ee,ex2=build(c.block(1).statement(),succs)
                    for e in ee: G.add_edge(nid,e)
                    exits=tx+ex2
                else: exits=tx+[nid]
            elif s.whileStatement():
                be,bx=build(s.whileStatement().block().statement(),[nid])
                for e in be: G.add_edge(nid,e)
                for x in bx: G.add_edge(x,nid)
                exits=[nid]
            elif s.forStatement():
                be,bx=build(s.forStatement().block().statement(),[nid])
                for e in be: G.add_edge(nid,e)
                for x in bx: G.add_edge(x,nid)
                exits=[nid]
        for e in exits:
            for s in succs: G.add_edge(e,s)
        return entries,exits
    build(tree.statement(),[])
    return G


# ───────────────────────────────────────────────────────────────────────────────
# 9. Z3 helpers for equivalence
# ───────────────────────────────────────────────────────────────────────────────
def _expr_to_z3(e, gv):
    if isinstance(e,int): return e
    if isinstance(e,str): return gv(e)
    _,_,L,op,R=e; Lz,Rz=_expr_to_z3(L,gv),_expr_to_z3(R,gv)
    return {
        "+":Lz+Rz,"-":Lz-Rz,"==":Lz==Rz,"!=":Lz!=Rz,
        "<":Lz<Rz,"<=":Lz<=Rz,">":Lz>Rz,">=":Lz>=Rz,
    }[op]

def final_map(ssa):
    last={}
    for inst in ssa:
        if inst[0]=="assign":
            nm=inst[1]; orig=nm.split("_",1)[0]; last[orig]=nm
    return last


# ───────────────────────────────────────────────────────────────────────────────
# 10. Flask routes
# ───────────────────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/workbench")
def workbench():
    return render_template("workbench.html")

@app.route("/verify")
def verify_page():
    return render_template("verify.html")

@app.route("/equiv")
def equiv_page():
    return render_template("equiv.html")


@app.route("/parse", methods=["POST"])
def parse_route():
    data = request.get_json()
    tree,errs = parse_program(data.get("program",""))
    if errs: return jsonify({"errors":errs}),400
    k=int(data.get("unroll",1))
    return jsonify({
        "unrolled": unroll_loops(tree,k),
        "origSSA":  generate_ssa(tree,k),
        "optSSA":   optimize_ssa(generate_ssa(tree,k)),
        "smt":      generate_smt(generate_ssa(tree,k)),
        "verification": dict(zip(["holds","witnesses"], verify_ssa(generate_ssa(tree,k)))),
        "cfgCode":   { n:list(adj) for n,adj in cfg_from_code(tree).adj.items() }
    })

# ── helper: prefix all SSA names so A and B don’t collide ───────────────────
def prefix_ssa(ssa, prefix):
    def pref(x):
        if isinstance(x, str) and not x.isdigit():
            return f"{prefix}_{x}"
        return x
    def recurse(e):
        if isinstance(e, tuple) and e[0] == "binop":
            _, _, L, op, R = e
            return ("binop", None, recurse(L), op, recurse(R))
        return pref(e)

    out = []
    for inst in ssa:
        tag = inst[0]
        if tag == "assign":
            _, v, rhs = inst
            out.append(("assign", pref(v), recurse(rhs)))
        elif tag == "store":
            _, arr, idx, val = inst
            out.append(("store", pref(arr), recurse(idx), recurse(val)))
        else:  # assert
            _, v, cond = inst
            out.append(("assert", pref(v), recurse(cond)))
    return out


# ── fixed Equivalence endpoint ───────────────────────────────────────────────
@app.route("/equiv-api", methods=["POST"])
def equivalence_api():
    data = request.get_json()
    k = int(data.get("unroll", 1))

    # 1) Parse both programs
    treeA, errsA = parse_program(data.get("progA", ""))
    treeB, errsB = parse_program(data.get("progB", ""))
    if errsA or errsB:
        return jsonify({"errors": errsA + errsB}), 400

    # 2) Generate SSA for each (with unrolling)
    ssaA = generate_ssa(treeA, k)
    ssaB = generate_ssa(treeB, k)

    # 3) Verify each separately (max 2 counter-examples)
    holdsA, exA = verify_ssa(ssaA, max_cex=2)
    holdsB, exB = verify_ssa(ssaB, max_cex=2)

    # 4) Equivalence = both hold or both fail
    equivalent = (holdsA == holdsB)

    # 5) Build response
    resp = {
        "equivalent": equivalent,
        "resultA": {
            "holds": holdsA,
            # if it failed, exA are counter-examples; if it held, exA are witnesses
            **({"counterexamples": exA} if not holdsA else {"witnesses": exA})
        },
        "resultB": {
            "holds": holdsB,
            **({"counterexamples": exB} if not holdsB else {"witnesses": exB})
        }
    }
    return jsonify(resp)


if __name__=="__main__":
    app.run(debug=True)
