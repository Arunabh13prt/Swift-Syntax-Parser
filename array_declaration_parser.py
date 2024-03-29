from ply import yacc
from array_declaration_lex import tokens

# Parsing rules
def p_declaration(p):
    '''declaration : VAR IDENTIFIER COLON LBRACKET data_type RBRACKET  EQUAL LBRACKET array_elements RBRACKET
                   | VAR IDENTIFIER EQUAL LBRACKET array_elements RBRACKET SEMICOLON
                   | VAR IDENTIFIER COLON LBRACKET data_type RBRACKET SEMICOLON
    '''

    p[0] = {'VAR': p[1], 'SEMICOLON' : p[9], 'COLON': p[3], 'LBRACKET': p[4], 'data_type': p[5], 'RBRACKET': p[6], 'EQUAL': p[7], 'array_elements': p[8], }


def p_data_type(p):
    '''data_type : INT
                 | FLOAT
                 | DOUBLE
                 | CHARACTER
                 | BOOL
                 | STRING'''
    if(len(p) == 5):
        p[0]= p[4]
    else:
        p[0] = None 
    

def p_array_elements(p):
    '''array_elements : empty
                      | array_elements element
                      | array_elements COMMA element'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = []

def p_element(p):
    '''element : NUMBER
               | STRING_VALUE'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    try:
        print(f"Syntax error at '{p.value}'")
    except:
        print("The given string is valid")
        exit(0)

parser = yacc.yacc()
