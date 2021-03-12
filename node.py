class LiteralNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"


class BoolNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"


class BinaryOperationNode:
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left}, {self.operator}, {self.right}"


class UnaryOperationNode:
    def __init__(self, operator, node):
        self.operator = operator
        self.node = node

    def __repr__(self):
        return f"{self.operator}:{self.node}"
