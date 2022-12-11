monkeys = []
round = 0
roundLimit = 20


class ThrowTest:
  def __init__(self, divisibleBy, trueThrow, falseThrow):
    self.divisibleBy = divisibleBy
    self.trueThrow = trueThrow
    self.falseThrow = falseThrow

  def decide(self, value):
    if value % self.divisibleBy == 0:
      return self.trueThrow
    return self.falseThrow


class Operation:
  def __init__(self, tokens):
    self.tokens = tokens

  def getOperandValue(self, operand, old):
    if operand == 'old':
      return old
    else:
      return int(operand)

  def calculate(self, old):
    lhs, op, rhs = self.tokens
    lhs = self.getOperandValue(lhs, old)
    rhs = self.getOperandValue(rhs, old)

    if op == '+':
      return lhs + rhs
    elif op == '*':
      return lhs * rhs


class Monkey:
  def __init__(self, items, operation: Operation, test: ThrowTest):
    self.items = items
    self.operation = operation
    self.test = test
    self.inspections = 0

  def inspectItems(self):
    ret = []

    while self.items:
      self.inspections += 1
      item = self.items.pop(0)
      item = self.operation.calculate(item)
      item = item // 3
      ret.append((item, self.test.decide(item)))

    return ret

  def getInspections(self):
    return self.inspections

  def receiveItem(self, item):
    self.items.append(item)


while True:
  try:
    line = input()
    assert (line == f'Monkey {len(monkeys)}:')

    startingItems = list(map(int, input().partition(': ')[2].split(',')))
    operationTokens = input().partition('new = ')[2].split()
    divisibleBy = int(input().partition('divisible by ')[2])
    trueThrow = int(input().partition('throw to monkey ')[2])
    falseThrow = int(input().partition('throw to monkey ')[2])

    operation = Operation(operationTokens)
    throwTest = ThrowTest(divisibleBy, trueThrow, falseThrow)
    monkeys.append(Monkey(startingItems, operation, throwTest))

    # Empty line after each case
    input()

  except EOFError:
    break

while round < roundLimit:
  round += 1

  for i in range(len(monkeys)):
    throws = monkeys[i].inspectItems()

    for throw in throws:
      item, recipient = throw
      monkeys[recipient].receiveItem(item)

for i, monkey in enumerate(monkeys):
  print(f'Monkey {i} inspected items {monkey.getInspections()} times.')

inspections = sorted(map(lambda monkey: monkey.getInspections(), monkeys))
monkeyBusiness = inspections.pop() * inspections.pop()

print(monkeyBusiness)
