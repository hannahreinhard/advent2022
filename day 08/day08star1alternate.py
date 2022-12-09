import numpy as np

with open('day08input.txt') as f:
    input = f.readlines()

forest = []
for line in input:
    line = line.replace('\n', '')
    forest.append([int(e) for e in line])

forest = np.array(forest)

visible = 0

for i in range(np.size(forest,0)):
    for j in range(np.size(forest,1)):
        if i == 0 or i == np.size(forest,0) - 1 or j == 0 or j == np.size(forest,1) - 1:
            visible += 1
            continue
        up = forest[0:i, j]
        right = forest[i, j+1:]
        down = forest[i+1:, j]
        left = forest[i, 0:j]
        surroundings = [max(up), max(right), max(down), max(left)]
        if forest[i][j] > np.min(surroundings):
            visible += 1

print(visible)