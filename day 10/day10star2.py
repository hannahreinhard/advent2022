with open('day10input.txt') as f:
    commands = f.readlines()

for i in range(len(commands)):
    commands[i] = commands[i].replace('\n', '')
    commands[i] = commands[i].split(' ')
    if len(commands[i]) > 1:
        commands[i][1] = int(commands[i][1])

register = 1
addition = 0
adding = False
cyclestr = ''

for cycle in range(1, 241):
    if abs(((cycle - 1) % 40) - register) <= 1:
        cyclestr += '##'
    else:
        cyclestr += '  '
    if not adding:
        command = commands.pop(0)
        if command[0] != 'noop':
            addition = command[1]
            adding = True
    elif adding:
        register += addition
        adding = False
    if len(cyclestr) == 80:
        print(cyclestr)
        cyclestr = ''