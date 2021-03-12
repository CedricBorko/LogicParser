from node import Literal
from token import TokenType


class Interpreter:
    def __init__(self, literals):
        self.literals = literals

    def read(self, node):
        method_name = f"read_{type(node).__name__}"
        method = getattr(self, method_name, self.no_read_method)
        return method(node)

    def no_read_method(self, node):
        raise Exception(f"No read_{type(node).__name__} method defined")

    def read_LiteralNode(self, node):
        return bool(self.literals[node.token.value])

    @staticmethod
    def read_BoolNode(node):
        return node.token.value

    def read_BinaryOperationNode(self, node):
        left = self.read(node.left)
        right = self.read(node.right)

        if node.operator.type_ == TokenType.AND:
            return bool(left and right)
        elif node.operator.type_ == TokenType.OR:
            return bool(left or right)
        elif node.operator.type_ == TokenType.XOR:
            return bool((left and not right) or (not left and right))
        elif node.operator.type_ == TokenType.EQUIVALENCE:
            return bool((left and right) or (not left and not right))
        elif node.operator.type_ == TokenType.IMPLICATION:
            return bool((left and right) or (not left and right) or (not left and not right))

    def read_UnaryOperationNode(self, node):
        value = self.read(node.literal)
        if node.operator.type_ == TokenType.NOT:
            return False if value else True
