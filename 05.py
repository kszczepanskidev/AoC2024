from math import ceil

from helpers import loadFile

input = loadFile(__file__)

rules = {}
while True:
    rule = input.pop(0).split('|')
    if rule == ['']:
        break

    page = rule[0]
    if page in rules:
        rules[page].append(rule[1])
    else:
        rules[page] = [rule[1]]

result = 0
for manual in input:
    pages = manual.split(',')
    ordered = True
    for it, page in enumerate(pages):
        if page not in rules:
            continue

        intersection = set(rules[page]).intersection(set(pages[:it]))
        if len(intersection) > 0:
            ordered = False
            break

    if ordered:
        result += int(pages[ceil((len(pages) - 1) / 2)])

print(result)
