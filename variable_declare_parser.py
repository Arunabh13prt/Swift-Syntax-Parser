import ply.yacc as yacc
from variable_declare_lex import tokens


def p_declaration_list(p):
    '''declaration_list : empty
                       | declaration_list declaration'''
    pass

def p_declaration(p):
    '''declaration : data_type IDENTIFIER optional_colon optional_initializer optional_Semicolon'''
    # p[0] = {'data_type': p[1], 'IDENTIFIER' : p[2],'optional_colon': p[3], 'optional_initializer': p[4], 'optional_Semicolon': p[5]}

def p_data_type(p):
    '''data_type : VAR
                 | LET '''
    p[0] = p[1]

def p_optional_colon(p):
    '''optional_colon : COLON data_type_2
                      | empty'''
    if(len(p) == 3):
        p[0]=p[2]
    else:
        p[0] = None

def p_data_type_2(p):
    '''data_type_2 : INT optional_equal_int optional_Semicolon
                   | DOUBLE optional_equal_double optional_Semicolon
                   | FLOAT optional_equal_float optional_Semicolon
                   | STRING optional_equal_string optional_Semicolon
                   | CHARACTER optional_equal_character optional_Semicolon
                   | BOOL optional_equal_bool optional_Semicolon'''
    p[0] = p[1] 
    

def p_optional_Semicolon(p):
    ''' optional_Semicolon : SEMICOLON
                           | empty'''
    if(len(p) == 5):
        p[0]=p[4]
    elif(len(p) == 4):
        p[0] = p[3]
    else:
        p[0]=None

def p_optional_equal_int(p):
    '''optional_equal_int : EQUAL NUMBER 
                          | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None

def p_optional_equal_double (p):
    ''' optional_equal_double : EQUAL FLOAT_NUMBER  
                              | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None


def p_optional_equal_float (p):
    ''' optional_equal_float : EQUAL FLOAT_NUMBER  
                             | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None


def p_optional_equal_string (p):
    ''' optional_equal_string : EQUAL STRING_VALUE 
                              | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None


def p_optional_equal_character(p):
    ''' optional_equal_character : EQUAL CHARACTER_VALUE
                                 | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None


def p_optional_equal_bool (p):
    ''' optional_equal_bool : EQUAL BOOL_VALUE  
                              | empty '''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = None



def p_optional_initializer(p):
    '''optional_initializer : EQUAL FLOAT_NUMBER
                            | EQUAL NUMBER
                            | EQUAL STRING_VALUE
                            | EQUAL BOOL_VALUE
                            | empty'''
    if len(p) == 4:
        p[0] = p[3]
    elif len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = None

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()


