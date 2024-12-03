from helpers import loadFile

from re import finditer

input = ''.join(loadFile(__file__))

do_regex = r"do\(\)"
dont_regex = r"don't\(\)"

disabled_ranges = []
do_positions = [m.start() for m in finditer(do_regex, input)]
dont_positions = [m.start() for m in finditer(dont_regex, input)]

for dont in dont_positions:
    if len(disabled_ranges) > 0 and dont < disabled_ranges[-1][1]:
        continue

    range_start = dont
    range_end = 0

    if len(do_positions) == 0:
        range_end = len(input)
        disabled_ranges.append((range_start, range_end))
        break

    while range_end < range_start:
        range_end = do_positions.pop(0)
    disabled_ranges.append((range_start, range_end))

result = 0
mul_regex = r"mul\((\d+),(\d+)\)"
mul_matches = finditer(mul_regex, input)
for match in mul_matches:
    position = match.start()
    is_enabled = True
    for range in disabled_ranges:
        if position > range[0] and position < range[1]:
            is_enabled = False
            break

    if is_enabled:
        pair = match.groups()
        result += int(pair[0]) * int(pair[1])
print(result)
