import ply.yacc as yacc
from if_loop_lex import tokens

# Parsing rules
def p_statement(p):
    '''
    statement : if_statement
              | if_else_statement
              | assignment_statement
    '''
    p[0] = p[1]

def p_if_statement(p):
    '''
    if_statement : IF LPAREN condition RPAREN LCURLY statements RCURLY
    '''
    p[0] = {'IF': p[1], 'LPAREN': p[2], 'condition': p[3], 'RPAREN': p[4], 'LCURLY': p[5], 'statements': p[6], 'RCURLY': p[7]}

def p_if_else_statement(p):
    '''
    if_else_statement : IF LPAREN condition RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY
    '''
    p[0] = {'IF': p[1], 'LPAREN': p[2], 'condition': p[3], 'RPAREN': p[4], 'LCURLY_IF': p[5], 'statements_if': p[6], 'RCURLY_IF': p[7], 'ELSE': p[8], 'LCURLY_ELSE': p[9], 'statements_else': p[10], 'RCURLY_ELSE': p[11]}

def p_condition(p):
    '''
    condition : expression
    '''
    p[0] = p[1]

def p_expression(p):
    '''
    expression : term
               | expression AND term
               | expression OR term
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {'operator': p[2], 'left': p[1], 'right': p[3]}

def p_term(p):
    '''
    term : factor
         | term LESSTHAN factor
         | term GREATERTHAN factor
         | term EQUALTO factor
         | term NOTEQUAL factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {'operator': p[2], 'left': p[1], 'right': p[3]}

# def p_factor(p):
#     '''
#     factor : LPAREN expression RPAREN
#            | NUMBER
#            | IDENTIFIER
#     '''
#     if len(p) == 2:
#         p[0] = p[1]
#     else:
#         p[0] = p[2]

def p_factor(p):
    '''
    factor : LPAREN expression RPAREN
           | NUMBER
           | IDENTIFIER
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {'LPAREN': p[1], 'expression': p[2], 'RPAREN': p[3]}



def p_assignment_statement(p):
    '''
    assignment_statement : IDENTIFIER EQUAL expression SEMICOLON
    '''
    p[0] = {'IDENTIFIER': p[1], 'EQUAL': p[2], 'expression': p[3], 'SEMICOLON': p[4]}

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# Error handling rule
def p_error(p):
    try:
        print(f"Syntax error at '{p.value}'")
    except:
        print("The given string is valid")
        exit(0)

# Build the parser
parser = yacc.yacc()
