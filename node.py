class LiteralNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"


class Literal:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class BoolNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"


class Boolean:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class BinaryOperationNode:
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left}, {self.operator}, {self.right})"


class UnaryOperationNode:
    def __init__(self, operator, literal):
        self.operator = operator
        self.literal = literal

    def __repr__(self):
        return f"({self.operator}: {self.literal})"
