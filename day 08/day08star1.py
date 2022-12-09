import numpy as np

with open('day08input.txt') as f:
    input = f.readlines()

forest = []
for line in input:
    line = line.replace('\n', '')
    forest.append([int(e) for e in line])

forest = np.array(forest)
visible = np.zeros_like(forest)

# up
for column in range(np.size(forest,1)):
    maxheight = -1
    for row in range(np.size(forest,0)):
        if forest[row][column] > maxheight:
            visible[row][column] = 1
            maxheight = forest[row][column]

# down
for column in range(np.size(forest,1)):
    maxheight = -1
    for row in range(np.size(forest,0)-1, 0, -1):
        if forest[row][column] > maxheight:
            visible[row][column] = 1
            maxheight = forest[row][column]

# left
for row in range(np.size(forest,0)):
    maxheight = -1
    for column in range(np.size(forest,1)):
        if forest[row][column] > maxheight:
            visible[row][column] = 1
            maxheight = forest[row][column]

# right
for row in range(np.size(forest,0)):
    maxheight = -1
    for column in range(np.size(forest,1)-1, 0, -1):
        if forest[row][column] > maxheight:
            visible[row][column] = 1
            maxheight = forest[row][column]

print(np.sum(visible))