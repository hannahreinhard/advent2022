with open('day09input.txt') as f:
    moves = f.readlines()

for i in range(len(moves)):
    moves[i] = moves[i].replace('\n', '')
    moves[i] = moves[i].split(' ')
    moves[i][1] = int(moves[i][1])

visited = [(0,0)]
xt, yt = 0, 0
xh, yh = 0, 0

for move in moves:
    for step in range(move[1]):
        if move[0] == 'U':
            yh += 1
            if yh - 1 > yt:
                yt += 1
                xt = xh
        elif move[0] == 'D':
            yh -= 1
            if yh + 1 < yt:
                yt -= 1
                xt = xh
        elif move[0] == 'R':
            xh += 1
            if xh - 1 > xt:
                xt += 1
                yt = yh
        else:
            xh -= 1
            if xh + 1 < xt:
                xt -= 1
                yt = yh
        if (xt,yt) not in visited:
            visited.append((xt,yt))

print(len(visited))