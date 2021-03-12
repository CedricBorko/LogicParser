class Token:
    def __init__(self, type_, value=None):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"{self.type_}: {self.value}"
        return f"{self.type_}"


class TokenType:
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    XOR = "XOR"
    IMPLICATION = "IMPLICATION"
    EQUIVALENCE = "EQUIVALENCE"
    TRUE = "TRUE"
    FALSE = "FALSE"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LITERAL = "LITERAL"


OPERATORS = {

    "*": TokenType.AND,
    "+": TokenType.OR,
    "^": TokenType.XOR,
    "!": TokenType.NOT,
    ">": TokenType.IMPLICATION,
    "=": TokenType.EQUIVALENCE,
    "0": TokenType.FALSE,
    "1": TokenType.TRUE,
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN

}
