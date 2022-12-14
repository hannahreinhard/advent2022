with open('day13input.txt') as f:
    input = f.readlines()

def comparepackets(packet1,packet2):
    correctorder = None
    while correctorder is None:
        if type(packet1) != type([]) and type(packet2) == type([]):
            packet1 = [packet1]
        if type(packet2) != type([]) and type(packet1) == type([]):
            packet2 = [packet2]
        if len(packet1) > 0 and len(packet2) > 0:
            lhs = packet1.pop(0)
            rhs = packet2.pop(0)
            if type(lhs) != type([]) and type(rhs) != type([]):
                if lhs < rhs:
                    correctorder = True
                elif lhs > rhs:
                    correctorder = False
                continue
            elif type(lhs) == type([]) and type(rhs == type([])):
                correctorder = comparepackets(lhs,rhs)
            elif type(lhs) == type([]) and type(rhs != type([])):
                correctorder = comparepackets(lhs, [rhs])
            elif type(lhs) != type([]) and type(rhs == type([])):
                correctorder = comparepackets([lhs], rhs)
            if correctorder is not None:
                break
        elif len(packet1) < len(packet2):
            correctorder = True
        elif len(packet1) > len(packet2):
            correctorder = False
        else:
            correctorder = None
            break
    return correctorder

correctpackets = 0

for pair in range(int((len(input)-1)/3)):
    packettxt1 = 'packet1 = ' + input[3*pair].replace('\n', '')
    packettxt2 = 'packet2 = ' + input[3*pair + 1]
    exec(packettxt1)
    exec(packettxt2)

    if comparepackets(packet1, packet2):
        correctpackets += pair + 1
        print(pair + 1)

print(correctpackets)