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

def column(column):
    global input
    return [row[column] for row in input]

start_position = (0, 0)
for it, row in enumerate(input):
    if guard in row:
        start_position = (row.index(guard), it)
        break

width = len(input[0]) - 1
height = len(input) - 1

loops = 0

# Put obstacle at every possible empty tile and check if it loops to 2.5B steps. Total brute force. Expected result: 2262
for x in range(len(input[0])):
    for y in range(len(input)):
        if input[x][y] == '#':
            continue

        current_position = start_position
        steps = 0
        maze = [row for row in input]
        maze[x] = maze[x][:y] + '#' + maze[x][y+1:]

        while True:
            steps += 1
            if steps >= 2500000000:
                loops += 1
                break

            match direction:
                case 0:
                    if current_position[1] == 0:
                        break
                    elif maze[current_position[1] - 1][current_position[0]] == '#':
                        direction = rotate(direction)
                    else:
                        current_position = (current_position[0], current_position[1] - 1)

                case 1:
                    if current_position[0] == width:
                        break
                    elif maze[current_position[1]][current_position[0] + 1] == '#':
                        direction = rotate(direction)
                    else:
                        current_position = (current_position[0] + 1, current_position[1])

                case 2:
                    if current_position[1] == height:
                        break
                    elif maze[current_position[1] + 1][current_position[0]] == '#':
                        direction = rotate(direction)
                    else:
                        current_position = (current_position[0], current_position[1] + 1)

                case 3:
                    if current_position[0] == 0:
                        break
                    elif maze[current_position[1]][current_position[0] - 1] == '#':
                        direction = rotate(direction)
                    else:
                        current_position = (current_position[0] - 1, current_position[1])

print(loops)
