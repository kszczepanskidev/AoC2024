from helpers import loadFile

input = (loadFile(__file__))

def count_occurrences(rows):
    count = 0
    for row in rows:
        count += len(list(find_all(row, "XMAS"))) + len(list(find_all(row, "SAMX")))
    return count

def find_all(rows, keyword):
    start = 0
    while True:
        start = rows.find(keyword, start)
        if start == -1: return
        yield start
        start += 1


def get_diagonals(rows):
    max_col = len(rows[0])
    max_row = len(rows)
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y].append(rows[y][x])
            bdiag[x-y-min_bdiag].append(rows[y][x])

    return fdiag + bdiag

horizontals = count_occurrences(input)
verticals = count_occurrences([''.join(r) for r in list(reversed(list(zip(*input))))])
diagonals = count_occurrences([''.join(r) for r in get_diagonals(input)])

print(horizontals + verticals + diagonals)
