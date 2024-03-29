import ply.lex as lex

tokens = (
    'VAR',
    'LET',
    'COLON',
    'INT',
    'FLOAT',
    'DOUBLE',
    'BOOL',
    'CHARACTER',
    'STRING',
    'IDENTIFIER',
    'FLOAT_NUMBER',
    'NUMBER',
    'STRING_VALUE',
    'CHARACTER_VALUE',
    'BOOL_VALUE',
    'EQUAL',
    'SEMICOLON',
)

t_ignore = ' \t\n'

def t_VAR(t):
    r'var'
    t.value = str(t.value)
    return t

def t_LET(t):
    r'let'
    t.value = str(t.value)
    return t

t_COLON = r':'

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

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t

def t_FLOAT_NUMBER(t):
    r'\d+\.\d+|\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)  
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING_VALUE(t):
    r'(\"[^\"]*\")'
    t.value = str(t.value)  
    return t

def t_CHARACTER_VALUE(t):
    r'[a-zA-Z]'
    t.value = str(t.value)
    return t

def t_BOOL_VALUE(t):
    r'True|False'
    t.value = t.value.lower()  
    return t


t_EQUAL = r'='
t_SEMICOLON = r';'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    cond1=0
    t.lexer.skip(1)

lexer = lex.lex()


