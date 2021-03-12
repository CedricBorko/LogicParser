# LogicParser
Parser and calculator for logical expressions

Possible Operators are:
 - ^ (XOR)
 - = (Equivalence, <->)
 - > (Implication, ->)
 - * (And, &&)
 - + (Or, ||)

The "and" operator is not mandatory between literals and parenthesis. a*b == ab, a(b+c) == a*(b+c)

Examples:

ab+c!a => (a && b) || (c && !a)
a>(b+c) => (a && (b + c)) || (!a && (b + c)) || (!a && !(b + c)) => !(a && !(b+c))
a^b => (a XOR b) => (a && !b) || (!a && b)