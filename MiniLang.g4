grammar MiniLang;

program
  : statement* EOF
  ;

statement
  : assignment
  | assertStatement
  | ifStatement
  | whileStatement
  | forStatement
  ;

assignment
  : (NAME | arrayAccess) ASSIGN expr SEMI
  ;

assertStatement
  : ASSERT LPAREN expr RPAREN SEMI
  ;

ifStatement
  : IF LPAREN expr RPAREN block (ELSE block)?
  ;

whileStatement
  : WHILE LPAREN expr RPAREN block
  ;

forStatement
  : FOR LPAREN
      (assignmentExpression)? SEMI
      expr? SEMI
      (assignmentExpression)?
    RPAREN block
  ;

assignmentExpression
  : (NAME | arrayAccess) ASSIGN expr
  ;

block
  : LBRACE statement* RBRACE
  ;

expr
  : equality
  ;

equality
  : relational (EQUALS relational)*
  ;

relational
  : additive ((LT | GT | LE | GE | NE) additive)*
  ;

additive
  : multiplicative ((PLUS | MINUS) multiplicative)*
  ;

multiplicative
  : atom
  ;

atom
  : NUMBER
  | arrayAccess
  | NAME
  | LPAREN expr RPAREN
  ;

arrayAccess
  : NAME LBRACK expr RBRACK
  ;

// Keywords
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
ASSERT  : 'assert';

// Operators & punctuation
ASSIGN  : ':=' ;
EQUALS  : '==' ;
NE      : '!=' ;
LT      : '<'  ;
GT      : '>'  ;
LE      : '<=' ;
GE      : '>=' ;
PLUS    : '+'  ;

// MINUS now accepts both ASCII '-' and Unicode '−'
MINUS   : '-'  
        | '−' 
        ;

LPAREN  : '('  ;
RPAREN  : ')'  ;
LBRACE  : '{'  ;
RBRACE  : '}'  ;
LBRACK  : '['  ;
RBRACK  : ']'  ;
SEMI    : ';'  ;

// Identifiers, numbers, whitespace
NAME    : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER  : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
