import itertools

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from token import OPERATORS

print(OPERATORS)


def calculate_result(res, literals):
    combinations = list(itertools.product([1, 0], repeat=len(literals)))
    truth_table = []

    for i in range(len(combinations) - 1, -1, -1):
        translator = {}
        for key_ in literals:
            translator[key_] = combinations[i][literals.index(key_)]

        interpreter = Interpreter(translator)
        truth_table.append([int(interpreter.read(res)), [translator[literal] for literal in literals]])

    knf_form, dnf_form = normal_forms(truth_table, literals)
    print("KNF:", knf_form)
    print("DNF:", dnf_form)
    if len(truth_table) > 1:
        print(' '.join(literals), "S")
        for entry in truth_table:
            print(' '.join(map(str, entry[1])), entry[0])


def normal_forms(table, literals):
    if len(table) == 1:
        return ("x\u2228¬x", "x\u2228¬x") if table[0][0] == 1 else ("False", "False")
    knf_result = []
    dnf_result = []
    for item in table:

        if item[0] == 0:
            sequence = "(" + '\u2228'.join([literals[i] if item[1][i] == 0 else "¬" + literals[i] for i in range(len(literals))]) + ")"
            knf_result.append(sequence)
        else:
            sequence = "(" + ''.join([literals[i] if item[1][i] == 1 else "¬" + literals[i] for i in range(len(literals))]) + ")"
            dnf_result.append(sequence)

    return '\u2227'.join(knf_result), '\u2228'.join(dnf_result)


while True:
    t = input("> ")
    lexer = Lexer(t)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    result = parser.parse()
    print(result)
    calculate_result(result, sorted(parser.literals))
