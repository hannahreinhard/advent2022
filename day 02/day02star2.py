f = open('day02input.txt')

rounds = f.readlines()

key1 = ['A', 'B', 'C']
key2 = [1, 2, 3]

score = 0

for round in rounds:
    opponent = key1.index(round[0])
    if round[2] == 'Z':
        score += 6 + key2[opponent - 2]
    elif round[2] == 'Y':
        score += 3 + key2[opponent]
    else:
        score += key2[opponent - 1]

print(score)