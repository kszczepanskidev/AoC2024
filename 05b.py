from math import ceil

from helpers import loadFile

input = loadFile(__file__)

# Read ordering rules.
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
    # Filter out ordered print orders.
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
        continue

    # Sort wrong print orders.
    temp = []
    for page in pages:
        if page not in rules:
            temp.append(page)
            continue

        # Pages already sorted that current page should precede.
        before_intersection = set(rules[page]).intersection(set(temp))

        # Already sorted pages that should precede current page.
        after_intersection = set([rule_page for rule_page in rules if page in rules[rule_page]])

        if len(before_intersection) > 0 or len(after_intersection) > 0:
            before_index = min([temp.index(rule_page) for rule_page in before_intersection] + [len(temp)])
            after_index = max([temp.index(rule_page) for rule_page in after_intersection if rule_page in temp] + [0])
            temp.insert(max(before_index, after_index), page)
            continue

        temp.insert(0, page)

    result += int(temp[ceil((len(temp) - 1) / 2)])


print(result)
