import numpy as np

with open('day12input.txt') as f:
    input = f.readlines()

map = []
for row,line in enumerate(input):
    line = line.replace('\n', '')
    mapline = []
    for column,char in enumerate(line):
        if char == 'S':
            start = (row, column, ord('a'))
            mapline.append(ord('a'))
        elif char == 'E':
            end = (row, column, ord('z'))
            mapline.append(ord('z'))
        else: 
            mapline.append(ord(char))
    map.append(mapline)

map = np.array(map)
shortestmap = np.full_like(map, 10000000, dtype=int)
shortestmap[start[0], start[1]] = 0
visitedmap = np.zeros_like(map, dtype=bool)
visitedmap[start[0], start[1]] = True
checklist = [start]

def checknum(x,y,z,newnumsteps):
    if newnumsteps < shortestmap[x, y]:
        shortestmap[x, y] = newnumsteps
    if not visitedmap[x, y]:
        checklist.append((x, y, z))
        visitedmap[x, y] = True

while len(checklist) > 0:
    checklist.sort(key=lambda a: shortestmap[a[0],a[1]])
    x,y,z = checklist.pop(0)
    newnumsteps = shortestmap[x, y] + 1
    if x != 0 and map[x-1, y] - 1 <= z:
        checknum(x-1, y, map[x-1, y], newnumsteps)
    if x != np.size(map, 0)-1 and map[x+1, y] - 1 <= z:
        checknum(x+1, y, map[x+1, y], newnumsteps)
    if y != 0 and map[x, y-1] - 1 <= z:
        checknum(x, y-1, map[x, y-1], newnumsteps)
    if y != np.size(map, 1)-1 and map[x, y+1] - 1 <= z:
        checknum(x, y+1, map[x, y+1], newnumsteps)
    if visitedmap[end[0],end[1]]:
        checklist.clear()

print(shortestmap[end[0],end[1]])