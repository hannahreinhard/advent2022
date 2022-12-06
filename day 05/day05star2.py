f = open('day05input.txt')

setup = True
setuplines = []

while setup:
    line = f.readline()
    setupline = ''
    if '[' in line:
        line = line.replace('\n', ' ')
        for i in range(0, int(len(line)/4)):
            box = line[4*i + 1]
            if box == ' ':
                setupline += ' '
            else:
                setupline += box
        setuplines.append(setupline)
    elif line == '\n':
        setup = False

boxcolumns = []

for column in range(len(setuplines[-1])):
    newcolumn = []
    for row in setuplines:
        if row[column] != ' ':
            newcolumn.append(row[column])
    newcolumn.reverse()
    boxcolumns.append(newcolumn)

moves = f.readlines()
f.close()

for line in moves:
    line = line.replace('\n', '')
    line = line.split(' ')
    movelist = []
    for movenum in range(int(line[1])):
        movelist.append(boxcolumns[int(line[3]) - 1].pop())
    movelist.reverse()
    boxcolumns[int(line[5]) - 1].extend(movelist)

endstr = ''
for column in boxcolumns:
    endstr += column[-1]

print(endstr)