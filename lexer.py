import string

from token import Token, TokenType, OPERATORS


class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self, steps=1):
        self.index += steps
        self.current_token = self.expression[self.index] if self.index < len(self.expression) else None

    def peek(self):
        try:
            return self.expression[self.index + 1]
        except IndexError:
            return None

    def look_back(self):
        try:
            return self.expression[self.index - 1]
        except IndexError:
            return None

    def generate_tokens(self):
        tokens = []

        while self.current_token is not None:

            if self.current_token in " \t":
                self.advance()

            elif self.current_token in OPERATORS:
                tokens.append(Token(OPERATORS[self.current_token]))
                if self.current_token in "01)":
                    next_ = self.peek()
                    if next_ is not None and next_ in string.ascii_letters + "!(":
                        tokens.append(Token(TokenType.AND))
                self.advance()

            elif self.current_token in string.ascii_letters:
                next_ = self.peek()
                if next_ is not None and next_ not in "+^>=*)":
                    tokens.append(Token(TokenType.LITERAL, self.current_token))
                    tokens.append(Token(TokenType.AND))
                else:
                    tokens.append(Token(TokenType.LITERAL, self.current_token))
                self.advance()

            else:
                print("ERR")
                return None

        return tokens
