# MiniLang Verification Workbench

A Flask-based workbench for parsing and verifying programs written in MiniLang. The app uses ANTLR4 to parse source code, transforms programs into SSA form, generates SMT-LIB constraints, and uses Z3 to check assertions and bounded program equivalence.

## Features

- Parses MiniLang programs with an ANTLR4 grammar.
- Reports syntax errors from the generated lexer and parser.
- Unrolls `for` and `while` loops with a configurable bound.
- Converts assignments into Static Single Assignment form.
- Applies constant propagation, common subexpression elimination, and dead-code elimination.
- Generates SMT-LIB constraints for integer program reasoning.
- Verifies `assert(...)` statements with Z3.
- Shows counterexamples or witnesses when verification fails or succeeds.
- Builds a control-flow graph for parsed programs.
- Checks bounded equivalence between two MiniLang programs.
- Provides browser pages for verification and equivalence workflows.

## MiniLang Syntax

```text
x := 5;
y := x + 3;

if (x > 2) {
    z := x - 1;
} else {
    z := 0;
}

while (y > 0) {
    y := y - 1;
}

for (i := 0; i < 5; i := i + 1) {
    s := s + i;
}

assert(z >= 0);
```

Supported constructs include integer variables, array access, arithmetic expressions, comparisons, `if`/`else`, `while`, `for`, and `assert`.

## Tech Stack

| Part | Tech |
| --- | --- |
| Language | Python |
| Web framework | Flask |
| Grammar | ANTLR4 |
| Parser runtime | antlr4-python3-runtime |
| Solver | Z3 |
| Graph model | NetworkX |
| Frontend | Jinja templates, Bootstrap, JavaScript |

## Project Structure

```text
.
|-- MiniLang.g4                  # MiniLang grammar
|-- MiniLangLexer.py             # Generated ANTLR lexer
|-- MiniLangParser.py            # Generated ANTLR parser
|-- MiniLangVisitor.py           # Generated ANTLR visitor base
|-- app.py                       # Flask app and verification pipeline
|-- requirements.txt             # Python dependencies
|-- antlr-4.13.2-complete.jar    # ANTLR tool for parser regeneration
|-- templates/                   # Browser pages
|-- static/                      # CSS and JavaScript assets
`-- README.md
```

## Install Dependencies

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Workflows

### Verify A Program

Open `/verify`, enter a MiniLang program, choose an unroll bound, and run the verifier.

The output includes:

- unrolled source
- original SSA form
- optimized SSA form
- SMT-LIB constraints
- verification result
- control-flow graph data

### Check Program Equivalence

Open `/equiv`, enter two MiniLang programs, choose an unroll bound, and run the equivalence checker.

The checker compares bounded final program states with Z3.

## API Endpoints

```text
POST /parse
Body: { "program": "<MiniLang code>", "unroll": <k> }

POST /equiv-api
Body: { "progA": "<MiniLang code>", "progB": "<MiniLang code>", "unroll": <k> }
```

## Regenerate Parser Files

Only needed after editing `MiniLang.g4`:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 MiniLang.g4
```

## Verification Pipeline

```text
MiniLang source
    |
    v
ANTLR4 parser
    |
    v
Loop unrolling
    |
    v
SSA transformation
    |
    v
Optimization passes
    |
    v
SMT-LIB generation
    |
    v
Z3 verification
```
