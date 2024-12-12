from enum import Enum

from helpers import loadFile

obstacle = '#'
guard = '^'

input = loadFile(__file__)

# 0 - UP | 1 - RIGHT | 2 - DOWN | 3 - LEFT
direction = 0

# Rotate 90° clockwise.
def rotate(direction):
    return (0 if direction == 3 else direction + 1)

current_position = (0, 0)
for it, row in enumerate(input):
    if guard in row:
        current_position = (row.index(guard), it)
        break

visited = []
width = len(input[0]) - 1
height = len(input) - 1

while True:
    visited.append(current_position)
    match direction:
        case 0:
            if current_position[1] == 0:
                break
            elif input[current_position[1] - 1][current_position[0]] == '#':
                direction = rotate(direction)
            else:
                current_position = (current_position[0], current_position[1] - 1)

        case 1:
            if current_position[0] == width:
                break
            elif input[current_position[1]][current_position[0] + 1] == '#':
                direction = rotate(direction)
            else:
                current_position = (current_position[0] + 1, current_position[1])

        case 2:
            if current_position[1] == height:
                break
            elif input[current_position[1] + 1][current_position[0]] == '#':
                direction = rotate(direction)
            else:
                current_position = (current_position[0], current_position[1] + 1)

        case 3:
            if current_position[0] == 0:
                break
            elif input[current_position[1]][current_position[0] - 1] == '#':
                direction = rotate(direction)
            else:
                current_position = (current_position[0] - 1, current_position[1])

print(len(set(visited)))
