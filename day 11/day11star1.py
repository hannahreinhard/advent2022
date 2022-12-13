from numpy import fromstring

class Monkey:

    def __init__(self, itemlist, operator, operand, test, recipients):
        self.itemlist = itemlist
        self.operator = operator
        self.operand = operand
        self.test = test
        self.recipients = recipients
        self.inspections = 0
        if operator == '+' and operand.isnumeric():
            self.operation = lambda x: x + int(operand)
        elif operator == '*' and operand.isnumeric():
            self.operation = lambda x: x * int(operand)
        else:
            self.operation = lambda x: x * x

    def taketurn(self):
        throwlist = []
        for item in self.itemlist:
            item = self.operation(item)
            item = item // 3
            if item % self.test == 0:
                throwlist.append([self.recipients[0],item])
            else:
                throwlist.append([self.recipients[1],item])
            self.inspections += 1
        self.itemlist = []
        return throwlist


def throw(monkey, monkeylist):
    throwlist = monkey.taketurn()
    for throw in throwlist:
        monkeylist[throw[0]].itemlist.append(throw[1])


f = open('day11input.txt')
input = f.readlines()
f.close()
for line in range(len(input)):
    input[line] = input[line].replace('\n', '')

monkeylist = []
for monkey in range(int((len(input) + 1)/7)):
    # parse starting items
    startingitems = input[7*monkey + 1].split(':')[1]
    itemlist = list(fromstring(startingitems[1:], dtype=int, sep=', '))

    # parse operation
    operationline = input[7*monkey + 2]
    operator = operationline[operationline.find('old') + 4]
    operand = operationline[operationline.find('old') + 6:]

    # parse test
    testline = input[7*monkey + 3]
    testnumber = int(testline[testline.find('by') + 3:])
    iftrue = int(input[7*monkey + 4][-1])
    iffalse = int(input[7*monkey + 5][-1])

    monkeylist.append(Monkey(itemlist, operator, operand, testnumber, [iftrue, iffalse]))

for i in range(20):
    for monkey in monkeylist:
        throw(monkey, monkeylist)

monkeylist.sort(key = lambda x: x.inspections, reverse = True)
monkeybusiness = monkeylist[0].inspections * monkeylist[1].inspections
print(monkeybusiness)