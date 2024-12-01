def loadFile(name):
    return [l.strip() for l in open(f'{name.replace("b.py","").replace(".py","")}-in.txt').readlines()]

def chunks(array, size):
    for i in range(0, len(array), size):
        yield array[i:i+size]

def flatten(list):
    return [item for sublist in list for item in sublist]

def transpose(grid):
    return [''.join(list(i)) for i in zip(*grid)]
