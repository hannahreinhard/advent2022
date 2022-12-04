f = open('day04input.txt')
pairs = f.readlines()
f.close()

count = 0

for pair in pairs:
    elflist = pair.split(',')
    elflist[1] = elflist[1].replace('\n', '')
    range1 = elflist[0].split('-')
    range1 = [int(e) for e in range1]
    range2 = elflist[1].split('-')
    range2 = [int(e) for e in range2]
    if range1[0] <= range2[0] and range1[1] >= range2[0]:
        count += 1
    elif range2[0] <= range1[0] and range2[1] >= range1[0]:
        count += 1

print(count)