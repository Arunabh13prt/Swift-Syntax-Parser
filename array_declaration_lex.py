import ply.lex as lex

# List of token names
tokens = (
    'VAR',
    'INT',
    'FLOAT',
    'DOUBLE',
    'BOOL',
    'CHARACTER',
    'STRING',
    'IDENTIFIER',
    'SEMICOLON',
    'COLON',
    'LBRACKET',
    'RBRACKET',
    'EQUAL',
    'NUMBER',
    'STRING_VALUE',
    'COMMA',
)

# Regular expression for tokens
def t_VAR(t):
    r'var'
    t.value = str(t.value)
    return t

def t_INT(t):
    r'Int'
    t.value = str(t.value)
    return t

def t_FLOAT(t):
    r'Float'
    t.value = str(t.value)
    return t

def t_DOUBLE(t):
    r'Double'
    t.value = str(t.value)
    return t

def t_BOOL(t):
    r'Bool'
    t.value = str(t.value)
    return t

def t_CHARACTER(t):
    r'Character'
    t.value= str(t.value)
    return t

def t_STRING(t):
    r'String'
    t.value = str(t.value)
    return t

t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SEMICOLON = r';'
t_COLON = r':'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUAL = r'='
t_NUMBER = r'\d+'
t_STRING_VALUE = r'"[^"]*"'
t_COMMA = r','

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()




