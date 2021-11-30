import token
from lex import *
from tokentype import *

def main():
    #input = "IF+-<>13241654algo*THEN"
    file = open("./code.mu","r")
    input = file.read()


    lexer = Lexer(input)
    token = lexer.getToken()
    cont = 0
    while token.kind != TokenType.EOF:
        print("Token Type: {} , Content: {}".format(token.kind, token.text))
        token = lexer.getToken()
        cont+=1
    print("Number tokens found: {}".format(cont))
main()