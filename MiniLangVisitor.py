# Generated from MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#statement.
    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignment.
    def visitAssignment(self, ctx:MiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assertStatement.
    def visitAssertStatement(self, ctx:MiniLangParser.AssertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ifStatement.
    def visitIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#forStatement.
    def visitForStatement(self, ctx:MiniLangParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:MiniLangParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expr.
    def visitExpr(self, ctx:MiniLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#equality.
    def visitEquality(self, ctx:MiniLangParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#relational.
    def visitRelational(self, ctx:MiniLangParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#additive.
    def visitAdditive(self, ctx:MiniLangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#multiplicative.
    def visitMultiplicative(self, ctx:MiniLangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#atom.
    def visitAtom(self, ctx:MiniLangParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniLangParser.ArrayAccessContext):
        return self.visitChildren(ctx)



del MiniLangParser