f = open('day03input.txt')

rucksacks = f.readlines()
priority = 0

# lowercase: 97 to 122
# uppercase 65 to 90
for group in range(int(len(rucksacks)/3)):
    elf1 = rucksacks[3*group]
    elf2 = rucksacks[3*group + 1]
    elf3 = rucksacks[3*group + 2]
    for item in elf1:
        if item in elf2 and item in elf3:
            itemnum = ord(item)
            if itemnum > 96:
                priority += itemnum - 96
            else:
                priority += itemnum - 38
            break

print(priority)