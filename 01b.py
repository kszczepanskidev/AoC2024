from helpers import loadFile
input = loadFile(__file__)

result = 0

left, right = zip(*[line.split('   ') for line in input])

for l in left:
    count = len([n for n in right if n == l])
    result += int(l) * count

print(result)
