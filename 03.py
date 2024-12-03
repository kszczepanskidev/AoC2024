from helpers import loadFile

from re import finditer

input = ''.join(loadFile(__file__))

regex = r"mul\((\d+),(\d+)\)"

matches = finditer(regex, input)

result = 0
for pair in [m.groups() for m in matches]:
    result += int(pair[0]) * int(pair[1])

print(result)
