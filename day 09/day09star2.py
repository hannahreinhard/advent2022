import numpy as np

with open('day09input.txt') as f:
    moves = f.readlines()

totalvert = 0
totalhorz = 0
for i in range(len(moves)):
    moves[i] = moves[i].replace('\n', '')
    moves[i] = moves[i].split(' ')
    moves[i][1] = int(moves[i][1])

visited = [[0,0]]
knots = np.zeros((10,2), dtype=int)

for move in moves:
    for step in range(move[1]):
        # move knot 0
        if move[0] == 'U':
            knots[0][1] += 1
        elif move[0] == 'D':
            knots[0][1] -= 1
        elif move[0] == 'R':
            knots[0][0] += 1
        else:
            knots[0][0] -= 1
        # move the rest of the knots
        for i in range(1,10):
            xh, yh = knots[i-1][0], knots[i-1][1]
            xt, yt = knots[i][0], knots[i][1]
            if xh > xt + 1:
                xt += 1
                if abs(yh-yt) < 2:
                    yt = yh
            elif xh < xt - 1:
                xt -= 1
                if abs(yh-yt) < 2:
                    yt = yh
            if yh > yt + 1:
                yt += 1
                if abs(knots[i-1][0]-knots[i][0]) < 2:
                    xt = xh
            elif yh < yt - 1:
                yt -= 1
                if abs(knots[i-1][0]-knots[i][0]) < 2:
                    xt = xh
            knots[i][0], knots[i][1] = xt, yt
        if [xt,yt] not in visited:
            visited.append([xt,yt])

print(len(visited))