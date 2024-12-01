from helpers import loadFile
input = loadFile(__file__)

left, right = zip(*[line.split('   ') for line in input])
left = sorted([int(v) for v in left])
right = sorted([int(v) for v in right])

result = 0

for l, r in zip(left, right):
    result += abs(l - r)

print(result)
