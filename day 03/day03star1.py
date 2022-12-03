f = open('day03input.txt')

rucksacks = f.readlines()
priority = 0

# lowercase: 97 to 122
# uppercase 65 to 90
for rucksack in rucksacks:
    pocket1 = rucksack[0:int(len(rucksack)/2)]
    pocket2 = rucksack[int(len(rucksack)/2):]
    for item in pocket1:
        if item in pocket2:
            itemnum = ord(item)
            if itemnum > 96:
                priority += itemnum - 96
            else:
                priority += itemnum - 38
            break

print(priority)