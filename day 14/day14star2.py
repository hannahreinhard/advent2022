import numpy as np

def dropsand(map, minx):
    currentcoord = [500, 0]
    atrest = False
    lastsand = False
    while not atrest:
        if currentcoord[1]-minx-1 < 0 or currentcoord[1]-minx+1 > np.size(map, 1):
            newcol = np.zeros((len(map[:,0]), 1), dtype=int)
            newcol[-1] = 2
            map = np.concatenate((newcol,map,newcol), axis=1)
            minx -= 1
        if map[currentcoord[1]+1, currentcoord[0]-minx] == 0:
            currentcoord = [currentcoord[0], currentcoord[1]+1]
        elif map[currentcoord[1]+1, currentcoord[0]-minx-1] == 0:
            currentcoord = [currentcoord[0]-1, currentcoord[1]+1]
        elif map[currentcoord[1]+1, currentcoord[0]-minx+1] == 0:
            currentcoord = [currentcoord[0]+1, currentcoord[1]+1]
        else:
            atrest = True
            map[currentcoord[1], currentcoord[0]-minx] = 1
            if currentcoord == [500, 0]:
                lastsand = True
    return map, lastsand, minx

with open('day14input.txt') as f:
    input = f.readlines()

directionlist = []
minx, maxx = 500, 0
maxy = 0
for line in input:
    line = line.replace('\n', '')
    line = line.split(' -> ')
    direction = []
    for point in line:
        point = point.split(',')
        direction.append([int(point[0]), int(point[1])])
        if int(point[0]) < minx:
            minx = int(point[0])
        if int(point[0]) > maxx:
            maxx = int(point[0])
        if int(point[1]) > maxy:
            maxy = int(point[1])
    directionlist.append(direction)

map = np.zeros((3+maxy, 1+maxx-minx), dtype=int)
map[-1, :] = 2
for direction in directionlist:
    for i in range(len(direction)-1):
        [x1, y1] = direction[i]
        [x2, y2] = direction[i+1]
        if x1 != x2:
            for x in range(min([x1, x2]), max([x1, x2]) + 1):
                map[y1, x - minx] = 2
        elif y1 != y2:
            for y in range(min([y1, y2]), max([y1, y2]) + 1):
                map[y, x1 - minx] = 2

lastsand = False
sandcounter = 0
while not lastsand:
    map, lastsand, minx = dropsand(map, minx)
    sandcounter += 1

print(sandcounter)