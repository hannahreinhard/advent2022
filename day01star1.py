f = open('day01input1.txt')

elfsum = 0
biggest = 0

for line in f:
    if line == '\n':
        if elfsum > biggest:
            biggest = elfsum
        elfsum = 0
    else:
        line = line.replace('\n', '')
        elfsum += int(line)

if elfsum > biggest:
    biggest = elfsum
    
print(biggest)

