import numpy as np

with open('day08input.txt') as f:
    input = f.readlines()

forest = []
for line in input:
    line = line.replace('\n', '')
    forest.append([int(e) for e in line])

forest = np.array(forest)

highscore = 0

for i in range(1, np.size(forest,0) - 1):
    for j in range(1, np.size(forest,1) - 1):
        up = forest[i-1::-1, j]
        down = forest[i+1:, j]
        left = forest[i, j-1::-1]
        right = forest[i, j+1:]
        viewlist = [up, down, left, right]
        score = 0
        totalscore = 1
        for view in viewlist:
            for tree in view:
                if tree < forest[i][j]:
                    score += 1
                else:
                    score += 1
                    break
            totalscore *= score
            score = 0
        if totalscore > highscore:
            highscore = totalscore

print(highscore)