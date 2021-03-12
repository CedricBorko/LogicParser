import itertools

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from token import OPERATORS

print(OPERATORS)


def calculate_result(res, literals):
    combinations = list(itertools.product([0, 1], repeat=len(literals)))
    truth_table = []
    for i in range(len(combinations) - 1, -1, -1):
        translator = {}
        for key_ in literals:
            translator[key_] = combinations[i][literals.index(key_)]

        interpreter = Interpreter(translator)
        truth_table.append([int(interpreter.read(res)), [translator[literal] for literal in literals]])

    print(' '.join(literals), "S")
    for entry in truth_table:
        print(' '.join(map(str, entry[1])), entry[0])


def equivalence(a, b):
    return (a and b) or (not a and not b)


def implication(a, b):
    return (a and b) or (not a and b) or (not a and not b)


def exclusive_or(a, b):
    return (a and not b) or (not a and b)


while True:
    t = input("> ")
    lexer = Lexer(t)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    result = parser.parse()
    calculate_result(result, parser.literals)
