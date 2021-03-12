from node import BinaryOperationNode, UnaryOperationNode, LiteralNode, BoolNode
from token import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.literals = []
        self.advance()

    def advance(self, steps=1):
        self.index += steps
        self.current_token = self.tokens[self.index] if self.index < len(self.tokens) else None

    def parse(self):
        return self.or_operator()

    def or_operator(self):
        left = self.and_operator()

        while self.current_token is not None and self.current_token.type_ in (TokenType.OR,
                                                                              TokenType.EQUIVALENCE,
                                                                              TokenType.IMPLICATION):
            op = self.current_token
            self.advance()
            right = self.and_operator()
            left = BinaryOperationNode(left, op, right)

        return left

    def and_operator(self):
        left = self.negation()

        while self.current_token is not None and self.current_token.type_ in (TokenType.AND, TokenType.XOR):
            op = self.current_token
            self.advance()
            right = self.negation()
            left = BinaryOperationNode(left, op, right)

        return left

    def negation(self):
        token = self.current_token
        if token.type_ == TokenType.NOT:
            self.advance()
            n = self.negation()
            return UnaryOperationNode(token, n)

        return self.atom()

    def atom(self):
        token = self.current_token

        if token.type_ == TokenType.LITERAL:
            self.advance()
            if token.value not in self.literals:
                self.literals.append(token.value)
            return LiteralNode(token)

        elif token.type_ in (TokenType.TRUE, TokenType.FALSE):
            self.advance()
            return BoolNode(token)

        elif token.type_ == TokenType.LPAREN:
            self.advance()
            expr = self.or_operator()

            if self.current_token.type_ == TokenType.RPAREN:
                self.advance()
                return expr
