from if_loop_lex import lexer
from if_loop_parser import parser

if __name__ == "__main__":
    while True:
        try:
            data = input("Enter a Swift variable declaration: ")
        except EOFError:
            break
        if not data:
            continue

        lexer.input(data)
        result = parser.parse(data, lexer=lexer)
    

# import ply.lex as lex
# import ply.yacc as yacc

# # List of tokens
# tokens = (
#     'VARIABLE_DECLARATION',
#     'IF_STATEMENT',
#     'FUNCTION_DECLARATION',
#     'FUNCTION_DEF',
#     'FOR_LOOP',
#     'OTHER',  # Catch-all for any other characters
# )

# # Regular expressions for Swift constructs
# t_VARIABLE_DECLARATION = r'(var|let)\s+[a-zA-Z_][a-zA-Z_0-9]*\s*:\s*[a-zA-Z_][a-zA-Z_0-9]*(\s*=\s*[^\s;]+)?\s*;'
# t_IF_STATEMENT = r'if\s*\(.*\)\s*{[^}]*}'
# t_FUNCTION_DECLARATION = r'func\s+[a-zA-Z_][a-zA-Z_0-9]*\s*\([^)]*\)\s*(->\s*[a-zA-Z_][a-zA-Z_0-9]*)?\s*{[^}]*}'
# t_FUNCTION_DEF = r'func\s+[a-zA-Z_][a-zA-Z_0-9]*\s*\([^)]*\)\s*(->\s*[a-zA-Z_][a-zA-Z_0-9]*)?\s*{[^}]*}'
# t_FOR_LOOP = r'for\s+[a-zA-Z_][a-zA-Z_0-9]*\s+in\s+[a-zA-Z_][a-zA-Z_0-9]*\s*{[^}]*}'
# t_OTHER = r'.'

# # Error handling
# def t_error(t):
#     print(f"Illegal character: {t.value[0]}")
#     t.lexer.skip(1)

# # Build the lexer
# lexer = lex.lex()

# def p_construct(p):
#     '''
#     construct : VARIABLE_DECLARATION
#               | IF_STATEMENT
#               | FUNCTION_DECLARATION
#               | FUNCTION_DEF
#               | FOR_LOOP
#               | OTHER
#     '''
#     pass  # Do nothing for now

# # Error handling in parser
# def p_error(p):
#     print("Invalid construct")

# # Build the parser
# parser = yacc.yacc()

# if __name__ == "__main__":
#     code = input("Enter a Swift construct: ")
    
#     lexer.input(code)
#     token_found = False

#     for token in lexer:
#         if token.type != 'OTHER':
#             token_found = True
#             if token.type == 'VARIABLE_DECLARATION':
#                 print("Valid Swift Variable Declaration")
#             elif token.type == 'IF_STATEMENT':
#                 print("Valid Swift If Statement")
#             elif token.type == 'FUNCTION_DECLARATION':
#                 print("Valid Swift Function Declaration")
#             elif token.type == 'FUNCTION_DEF':
#                 print("Valid Swift Function Def")
#             elif token.type == 'FOR_LOOP':
#                 print("Valid Swift For Loop")
    
#     if not token_found:
#         print("Invalid")
