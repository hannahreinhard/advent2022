with open('day10input.txt') as f:
    commands = f.readlines()

for i in range(len(commands)):
    commands[i] = commands[i].replace('\n', '')
    commands[i] = commands[i].split(' ')
    if len(commands[i]) > 1:
        commands[i][1] = int(commands[i][1])

register = 1
signalstrengthsum = 0
addition = 0
adding = False

for cycle in range(1, 221):
    if (cycle + 20) % 40 == 0:
        signalstrengthsum += cycle*register
    if not adding:
        command = commands.pop(0)
        if command[0] == 'noop':
            continue
        else:
            addition = command[1]
            adding = True
    elif adding:
        register += addition
        adding = False

print(signalstrengthsum)