import ply.lex as lex

# List of token names
tokens = (
    'IF',
    'ELSE',
    'LPAREN',
    'RPAREN',
    'LCURLY',
    'RCURLY',
    'IDENTIFIER',
    'EQUAL',
    'NUMBER',
    'LESSTHAN',
    'GREATERTHAN',
    'EQUALTO',
    'NOTEQUAL',
    'AND',
    'OR',
    'NOT',
    'SEMICOLON',
)

# Regular expression rules for tokens
t_IF = r'if'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUAL = r'=='
t_NUMBER = r'\d+'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_EQUALTO = r'='
t_NOTEQUAL = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_SEMICOLON = r';'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
