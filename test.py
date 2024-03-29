import ply.lex as lex
import ply.yacc as yacc

# List of tokens
tokens = (
    'VARIABLE_DECLARATION',
    'IF_STATEMENT',
    'FUNCTION_DECLARATION',
    'FUNCTION_DEF',
    'FOR_LOOP',
    'OTHER',  # Catch-all for any other characters
)

# Regular expressions for tokens
t_VARIABLE_DECLARATION = r'(int|char)\s[a-zA-Z_]=(\'[a-zA-Z_0-9]\'|[0-9]+)'
t_IF_STATEMENT = r'if\s*\([^)]\)\s{[^}]*}'
t_FUNCTION_DECLARATION = r'(int|void)\s[a-zA-Z_][a-zA-Z_0-9]\s\([^)]\)\s;'
t_FUNCTION_DEF = r'(int|void)\s[a-zA-Z_][a-zA-Z_0-9]\s\([^)]\)\s{[^}]*};'
t_FOR_LOOP = r'for\s*\([^)]\)\s{[^}]*}'
t_OTHER = r'.'

# Error handling
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def p_construct(p):
    '''
    construct : VARIABLE_DECLARATION
              | IF_STATEMENT
              | FUNCTION_DECLARATION
              | FUNCTION_DEF
              | FOR_LOOP
              | OTHER
    '''
    pass  # Do nothing for now

# Error handling in parser
def p_error(p):
    print("Invalid construct")

# Build the parser
parser = yacc.yacc()


if __name__ == "_main_":
    code = input("Enter a C++ construct: ")
    
    lexer.input(code)
    token_found = False

    for token in lexer:
        if token.type != 'OTHER':
            token_found = True
            if token.type == 'VARIABLE_DECLARATION':
                print("Valid and Variable Declaration")
            elif token.type == 'IF_STATEMENT':
                print("Valid and If Statement")
            elif token.type == 'FUNCTION_DECLARATION':
                print("Valid and Function Declaration")
            elif token.type == 'FUNCTION_DEF':
                print("Valid and Function Def")
            elif token.type == 'FOR_LOOP':
                print("Valid and For Loop")
    
    if not token_found:
        print("Invalid")