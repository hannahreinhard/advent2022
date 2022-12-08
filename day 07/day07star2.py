f = open('day07input.txt')

dirdict = {}
inlist = []
dupecount = 0

for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    if line[0].isnumeric():
        for dir in inlist:
            dirdict[dir] += int(line[0])
    elif line[-1] == '..':
        inlist.pop()
    elif line[1] == 'cd':
        if line[-1] in dirdict.keys():
            line[-1] += str(dupecount)
            dupecount += 1
        dirdict[line[-1]] = 0
        inlist.append(line[-1])

f.close()

totalsize =  dirdict['/']
deletethreshold = 30000000 - (70000000 - totalsize)
deletable = []

for dirsize in dirdict.values():
    if dirsize >= deletethreshold:
        deletable.append(dirsize)

deletable.sort()
print(deletable[0])