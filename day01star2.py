f = open('day01input1.txt')

elfsum = 0
elflist = []

for line in f:
    if line == '\n':
        elflist.append(elfsum)
        elfsum = 0
    else:
        line = line.replace('\n', '')
        elfsum += int(line)

elflist.append(elfsum)

elflist.sort(reverse=True)
    
print(sum(elflist[0:3]))