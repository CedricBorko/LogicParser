from lexer import Lexer
from token import OPERATORS

print(OPERATORS)

while True:
    t = input("> ")
    l = Lexer(t)
    print(l.generate_tokens())