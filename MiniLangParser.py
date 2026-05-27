# Generated from MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,151,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,3,2,50,8,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,69,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,80,8,6,1,6,1,6,3,6,84,8,6,1,
        6,1,6,3,6,88,8,6,1,6,1,6,1,6,1,7,1,7,3,7,95,8,7,1,7,1,7,1,7,1,8,
        1,8,5,8,102,8,8,10,8,12,8,105,9,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,
        5,10,114,8,10,10,10,12,10,117,9,10,1,11,1,11,1,11,5,11,122,8,11,
        10,11,12,11,125,9,11,1,12,1,12,1,12,5,12,130,8,12,10,12,12,12,133,
        9,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,144,8,14,
        1,15,1,15,1,15,1,15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,0,2,1,0,8,12,1,0,13,14,152,0,35,1,0,0,0,2,45,1,0,
        0,0,4,49,1,0,0,0,6,55,1,0,0,0,8,61,1,0,0,0,10,70,1,0,0,0,12,76,1,
        0,0,0,14,94,1,0,0,0,16,99,1,0,0,0,18,108,1,0,0,0,20,110,1,0,0,0,
        22,118,1,0,0,0,24,126,1,0,0,0,26,134,1,0,0,0,28,143,1,0,0,0,30,145,
        1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,
        35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,
        0,0,40,46,3,4,2,0,41,46,3,6,3,0,42,46,3,8,4,0,43,46,3,10,5,0,44,
        46,3,12,6,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,
        0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,50,5,22,0,0,48,50,3,30,15,0,49,
        47,1,0,0,0,49,48,1,0,0,0,50,51,1,0,0,0,51,52,5,6,0,0,52,53,3,18,
        9,0,53,54,5,21,0,0,54,5,1,0,0,0,55,56,5,5,0,0,56,57,5,15,0,0,57,
        58,3,18,9,0,58,59,5,16,0,0,59,60,5,21,0,0,60,7,1,0,0,0,61,62,5,1,
        0,0,62,63,5,15,0,0,63,64,3,18,9,0,64,65,5,16,0,0,65,68,3,16,8,0,
        66,67,5,2,0,0,67,69,3,16,8,0,68,66,1,0,0,0,68,69,1,0,0,0,69,9,1,
        0,0,0,70,71,5,3,0,0,71,72,5,15,0,0,72,73,3,18,9,0,73,74,5,16,0,0,
        74,75,3,16,8,0,75,11,1,0,0,0,76,77,5,4,0,0,77,79,5,15,0,0,78,80,
        3,14,7,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,83,5,21,0,
        0,82,84,3,18,9,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,87,
        5,21,0,0,86,88,3,14,7,0,87,86,1,0,0,0,87,88,1,0,0,0,88,89,1,0,0,
        0,89,90,5,16,0,0,90,91,3,16,8,0,91,13,1,0,0,0,92,95,5,22,0,0,93,
        95,3,30,15,0,94,92,1,0,0,0,94,93,1,0,0,0,95,96,1,0,0,0,96,97,5,6,
        0,0,97,98,3,18,9,0,98,15,1,0,0,0,99,103,5,17,0,0,100,102,3,2,1,0,
        101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,
        104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,18,0,0,107,17,1,0,0,0,
        108,109,3,20,10,0,109,19,1,0,0,0,110,115,3,22,11,0,111,112,5,7,0,
        0,112,114,3,22,11,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,1,0,
        0,0,115,116,1,0,0,0,116,21,1,0,0,0,117,115,1,0,0,0,118,123,3,24,
        12,0,119,120,7,0,0,0,120,122,3,24,12,0,121,119,1,0,0,0,122,125,1,
        0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,23,1,0,0,0,125,123,1,0,
        0,0,126,131,3,26,13,0,127,128,7,1,0,0,128,130,3,26,13,0,129,127,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,25,1,
        0,0,0,133,131,1,0,0,0,134,135,3,28,14,0,135,27,1,0,0,0,136,144,5,
        23,0,0,137,144,3,30,15,0,138,144,5,22,0,0,139,140,5,15,0,0,140,141,
        3,18,9,0,141,142,5,16,0,0,142,144,1,0,0,0,143,136,1,0,0,0,143,137,
        1,0,0,0,143,138,1,0,0,0,143,139,1,0,0,0,144,29,1,0,0,0,145,146,5,
        22,0,0,146,147,5,19,0,0,147,148,3,18,9,0,148,149,5,20,0,0,149,31,
        1,0,0,0,13,35,45,49,68,79,83,87,94,103,115,123,131,143
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'for'", 
                     "'assert'", "':='", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'+'", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "FOR", "ASSERT", 
                      "ASSIGN", "EQUALS", "NE", "LT", "GT", "LE", "GE", 
                      "PLUS", "MINUS", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "NAME", "NUMBER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_assertStatement = 3
    RULE_ifStatement = 4
    RULE_whileStatement = 5
    RULE_forStatement = 6
    RULE_assignmentExpression = 7
    RULE_block = 8
    RULE_expr = 9
    RULE_equality = 10
    RULE_relational = 11
    RULE_additive = 12
    RULE_multiplicative = 13
    RULE_atom = 14
    RULE_arrayAccess = 15

    ruleNames =  [ "program", "statement", "assignment", "assertStatement", 
                   "ifStatement", "whileStatement", "forStatement", "assignmentExpression", 
                   "block", "expr", "equality", "relational", "additive", 
                   "multiplicative", "atom", "arrayAccess" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    FOR=4
    ASSERT=5
    ASSIGN=6
    EQUALS=7
    NE=8
    LT=9
    GT=10
    LE=11
    GE=12
    PLUS=13
    MINUS=14
    LPAREN=15
    RPAREN=16
    LBRACE=17
    RBRACE=18
    LBRACK=19
    RBRACK=20
    SEMI=21
    NAME=22
    NUMBER=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194362) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MiniLangParser.AssignmentContext,0)


        def assertStatement(self):
            return self.getTypedRuleContext(MiniLangParser.AssertStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniLangParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniLangParser.ForStatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.assignment()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.assertStatement()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.ifStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.whileStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.forStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def NAME(self):
            return self.getToken(MiniLangParser.NAME, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(MiniLangParser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 47
                self.match(MiniLangParser.NAME)
                pass

            elif la_ == 2:
                self.state = 48
                self.arrayAccess()
                pass


            self.state = 51
            self.match(MiniLangParser.ASSIGN)
            self.state = 52
            self.expr()
            self.state = 53
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(MiniLangParser.ASSERT, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniLangParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_assertStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertStatement" ):
                return visitor.visitAssertStatement(self)
            else:
                return visitor.visitChildren(self)




    def assertStatement(self):

        localctx = MiniLangParser.AssertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assertStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MiniLangParser.ASSERT)
            self.state = 56
            self.match(MiniLangParser.LPAREN)
            self.state = 57
            self.expr()
            self.state = 58
            self.match(MiniLangParser.RPAREN)
            self.state = 59
            self.match(MiniLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(MiniLangParser.IF)
            self.state = 62
            self.match(MiniLangParser.LPAREN)
            self.state = 63
            self.expr()
            self.state = 64
            self.match(MiniLangParser.RPAREN)
            self.state = 65
            self.block()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 66
                self.match(MiniLangParser.ELSE)
                self.state = 67
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_whileStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MiniLangParser.WHILE)
            self.state = 71
            self.match(MiniLangParser.LPAREN)
            self.state = 72
            self.expr()
            self.state = 73
            self.match(MiniLangParser.RPAREN)
            self.state = 74
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.SEMI)
            else:
                return self.getToken(MiniLangParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def assignmentExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AssignmentExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AssignmentExpressionContext,i)


        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MiniLangParser.FOR)
            self.state = 77
            self.match(MiniLangParser.LPAREN)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 78
                self.assignmentExpression()


            self.state = 81
            self.match(MiniLangParser.SEMI)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 12615680) != 0):
                self.state = 82
                self.expr()


            self.state = 85
            self.match(MiniLangParser.SEMI)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 86
                self.assignmentExpression()


            self.state = 89
            self.match(MiniLangParser.RPAREN)
            self.state = 90
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def NAME(self):
            return self.getToken(MiniLangParser.NAME, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(MiniLangParser.ArrayAccessContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assignmentExpression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = MiniLangParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignmentExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 92
                self.match(MiniLangParser.NAME)
                pass

            elif la_ == 2:
                self.state = 93
                self.arrayAccess()
                pass


            self.state = 96
            self.match(MiniLangParser.ASSIGN)
            self.state = 97
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(MiniLangParser.LBRACE)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194362) != 0):
                self.state = 100
                self.statement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(MiniLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self):
            return self.getTypedRuleContext(MiniLangParser.EqualityContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MiniLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.equality()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.RelationalContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.RelationalContext,i)


        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.EQUALS)
            else:
                return self.getToken(MiniLangParser.EQUALS, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_equality

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = MiniLangParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.relational()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 111
                self.match(MiniLangParser.EQUALS)
                self.state = 112
                self.relational()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.AdditiveContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LT)
            else:
                return self.getToken(MiniLangParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.GT)
            else:
                return self.getToken(MiniLangParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.LE)
            else:
                return self.getToken(MiniLangParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.GE)
            else:
                return self.getToken(MiniLangParser.GE, i)

        def NE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NE)
            else:
                return self.getToken(MiniLangParser.NE, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MiniLangParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.additive()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0):
                self.state = 119
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7936) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 120
                self.additive()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.PLUS)
            else:
                return self.getToken(MiniLangParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.MINUS)
            else:
                return self.getToken(MiniLangParser.MINUS, i)

        def getRuleIndex(self):
            return MiniLangParser.RULE_additive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = MiniLangParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.multiplicative()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13 or _la==14:
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.multiplicative()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(MiniLangParser.AtomContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_multiplicative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = MiniLangParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multiplicative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MiniLangParser.NUMBER, 0)

        def arrayAccess(self):
            return self.getTypedRuleContext(MiniLangParser.ArrayAccessContext,0)


        def NAME(self):
            return self.getToken(MiniLangParser.NAME, 0)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = MiniLangParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atom)
        try:
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(MiniLangParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.arrayAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.match(MiniLangParser.NAME)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.match(MiniLangParser.LPAREN)
                self.state = 140
                self.expr()
                self.state = 141
                self.match(MiniLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MiniLangParser.NAME, 0)

        def LBRACK(self):
            return self.getToken(MiniLangParser.LBRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)


        def RBRACK(self):
            return self.getToken(MiniLangParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_arrayAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = MiniLangParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MiniLangParser.NAME)
            self.state = 146
            self.match(MiniLangParser.LBRACK)
            self.state = 147
            self.expr()
            self.state = 148
            self.match(MiniLangParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





