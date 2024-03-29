import ply.yacc as yacc
from function_declaration_lex import tokens


def p_declaration(p):
    '''declaration : FUNC IDENTIFIER LPAREN PARAMETERS RPAREN optional_pointer LCURLY function_body RCURLY 
                   | FUNC IDENTIFIER LPAREN PARAMETERS RPAREN SEMICOLON'''
    
    p[0] = {'IDENTIFIER' : p[1],'LPAREN': p[2], 'PARAMETERS': p[3], 'RPAREN': p[4], 'optional_pointer' :p[5] , 'LCURLY' : p[6], 'RCURLY' : p[7]}

def p_PARAMETERS(p):
    '''PARAMETERS : DEFAULT 
                  | Inout 
                  | VARIADIC'''
    
def p_DEFAULT(p):
    '''DEFAULT : optional_underscore IDENTIFIER COLON data_type COMMA DEFAULT 
               | optional_underscore IDENTIFIER COLON data_type '''


def p_optional_underscore(p):
    '''optional_underscore : UNDERSCORE 
                           | empty'''

def p_empty(p):
    'empty :'
    pass

def p_Inout(p):
    '''Inout : optional_underscore IDENTIFIER COLON INOUT data_type COMMA Inout
             | optional_underscore IDENTIFIER COLON INOUT data_type'''


def p_VARIDIC(p):
    '''VARIADIC : optional_underscore IDENTIFIER COLON data_type DOTS '''



def p_data_type(p):
    '''data_type : BOOL 
                 | INT 
                 | STRING 
                 | CHARACTER 
                 | FLOAT 
                 | DOUBLE'''


def p_optional_pointer(p):
    '''optional_pointer : POINTER data_type 
                        | empty'''


def p_function_body(p):
 '''function_body : statement
                  | statement function_body
                  | empty'''
   

def p_statement(p):
    '''statement : data_type2 IDENTIFIER SEMICOLON RCURLY COLON data_type EQUAL STRING_VALUE SEMICOLON
                 | data_type2 IDENTIFIER SEMICOLON '''


def p_data_type2(p):
    ''' data_type2 : LET
                   | VAR'''


def p_expression(p):
    ''' expression : IDENTIFIER '''
    

def p_error(p):
    try:
        print(f"Syntax error at '{p.value}'")
    except:
        print("Your string is valid")
        exit(0)

parser = yacc.yacc()
