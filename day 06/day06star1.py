f = open('day06input.txt')

signal = f.readline().replace('\n', '')

chunk = signal[0:3]
i = 3
startofpacket = False

while not startofpacket:
    chunk += signal[i]
    if chunk.count(chunk[0]) == 1 and chunk.count(chunk[1]) == 1 and chunk.count(chunk[2]) == 1:
        startofpacket = True
    else:
        chunk = chunk[1:]
    i += 1

print(i)