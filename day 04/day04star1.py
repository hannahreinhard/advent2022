f = open('day04input.txt')
pairs = f.readlines()
f.close()

count = 0

for pair in pairs:
    elflist = pair.split(',')
    elflist[1] = elflist[1].replace('\n', '')
    range1 = elflist[0].split('-')
    range2 = elflist[1].split('-')
    r2inr1 = int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])
    r1inr2 = int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1])
    if r2inr1 or r1inr2:
        count += 1

print(count)