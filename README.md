# LogicParser
Parser and calculator for logic expressions


Examples:

{'*': 'AND', '+': 'OR', '^': 'XOR', '!': 'NOT', '>': 'IMPLICATION', '=': 'EQUIVALENCE', '0': 'FALSE', '1': 'TRUE', '(': 'LPAREN', ')': 'RPAREN'}

input: a+bc+!c!a=a>b

a b c S
1 1 1 1
1 1 0 1
1 0 1 0
1 0 0 0
0 1 1 1
0 1 0 1
0 0 1 0
0 0 0 1

input: ab+c!a

a b c S
1 1 1 1
1 1 0 1
1 0 1 0
1 0 0 0
0 1 1 1
0 1 0 0
0 0 1 1
0 0 0 0
