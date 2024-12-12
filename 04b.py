from helpers import loadFile

input = loadFile(__file__)

result = 0

for i in range(1, len(input[0]) - 1):
    for j in range(1, len(input) - 1):
        if input[i][j] != 'A':
            continue

        diag1 = f'{input[i - 1][j - 1]}{input[i][j]}{input[i + 1][j + 1]}'
        diag2 = f'{input[i - 1][j + 1]}{input[i][j]}{input[i + 1][j - 1]}'

        if diag1 in ['MAS', 'SAM'] and diag2 in ['MAS', 'SAM']:
            result += 1

print(result)
