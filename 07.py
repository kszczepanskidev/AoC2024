from itertools import product
from helpers import loadFile

input = loadFile(__file__)

operators = ['+', '*']

def apply_ops(operators, values):
    result = int(values.pop(0))
    for op in operators:
        match op:
            case '+':
                result += int(values.pop(0))
            case '*':
                result *= int(values.pop(0))
    return result

result = 0
for line in [l.split(':') for l in input]:
    expected = int(line[0])
    values = line[1].strip().split(' ')
    combinations = product(operators, repeat=(len(values) - 1))

    for ops in combinations:
        if apply_ops(ops, values.copy()) == expected:
            result += expected
            break

print(result)
