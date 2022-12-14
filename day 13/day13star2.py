from copy import deepcopy
from functools import cmp_to_key
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
                    correctorder = -1
                elif lhs > rhs:
                    correctorder = 1
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
            correctorder = -1
        elif len(packet1) > len(packet2):
            correctorder = 1
        else:
            correctorder = None
            break
    return correctorder

def chancethewrapper(a,b):
    return comparepackets(deepcopy(a), deepcopy(b))

packetlist = []
for pair in range(int((len(input)-1)/3)):
    packettxt1 = 'packet1 = ' + input[3*pair].replace('\n', '')
    packettxt2 = 'packet2 = ' + input[3*pair + 1].replace('\n', '')
    exec(packettxt1)
    exec(packettxt2)
    packetlist.append(packet1)
    packetlist.append(packet2)

packetlist.append([[2]])
packetlist.append([[6]])
packetlist.sort(key=cmp_to_key(chancethewrapper))

print((packetlist.index([[2]])+1)*(packetlist.index([[6]])+1))