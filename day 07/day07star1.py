f = open('day07input.txt')

dirdict = {}
inlist = []
dupecount = 0

for line in f:
    line = line.replace('\n', '')
    line = line.split(' ')
    if line[0].isnumeric():
        print('|   '*len(inlist) + 'file ' + line[0])
        for dir in inlist:
            dirdict[dir] += int(line[0])
    elif line[-1] == '..':
        print('|   '*len(inlist) + 'total size: ' + str(dirdict[inlist[-1]]))
        inlist.pop()
    elif line[1] == 'cd':
        if line[-1] in dirdict.keys():
            line[-1] += str(dupecount)
            dupecount += 1
        dirdict[line[-1]] = 0
        inlist.append(line[-1])
        print('|   '*(len(inlist) - 1) + 'dir ' + line[-1])
print('total size: ' + str(dirdict['/']))

f.close()

total = 0
for dirsize in dirdict.values():
    if dirsize <= 100000:
        total += dirsize

print('total of directories with size <= 100000:', total)