f = open('day06input.txt')

signal = f.readline().replace('\n', '')

chunk = signal[0:13]
i = 13
startofmessage = False

inchunk = []
for char in chunk:
    if char not in inchunk:
        inchunk.append(char)

while not startofmessage:
    chunk += signal[i]
    if signal[i] not in inchunk and len(inchunk) == 13:
        startofmessage = True
    elif signal[i] not in inchunk:
        inchunk.append(signal[i])
    first = chunk[0]
    chunk = chunk[1:]
    if first not in chunk:
        inchunk.remove(first)
    i += 1

print(i)