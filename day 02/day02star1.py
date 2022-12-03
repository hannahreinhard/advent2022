f = open('day02input.txt')

rounds = f.readlines()

key1 = ['A', 'B', 'C']
key2 = ['X', 'Y', 'Z']

score = 0

for round in rounds:
    me = key2.index(round[2])
    if round[0] == key1[me - 1]:
        score += 6
    elif round[0] == key1[me]:
        score += 3
    score += me + 1

print(score)