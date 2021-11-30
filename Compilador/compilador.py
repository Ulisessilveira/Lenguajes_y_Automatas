import token
from lex import *
from tokentype import *

def main():
    input = "IF+-<>13241654algo*THEN"
    lexer = Lexer(input)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()