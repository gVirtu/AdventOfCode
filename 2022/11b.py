monkeys = []
round = 0
roundLimit = 10000

# Each item is now converted into an array:
#   for each monkey, store the item's worry value mod m


class MonkeyNumber:
  modulos = []

  def __init__(self, number):
    if isinstance(number, int):
      self.values = list(map(lambda m: number % m, MonkeyNumber.modulos))
    elif isinstance(number, MonkeyNumber):
      self.values = number.values

  # Define MonkeyNumber + int as adding to each value in array, then mod m
  # Define MonkeyNumber + MonkeyNumber as adding values by index, then mod m
  def __add__(self, rhs):
    ret = MonkeyNumber(self)
    if isinstance(rhs, int):
      for i in range(len(self.values)):
        ret.values[i] = (self.values[i] + rhs) % MonkeyNumber.modulos[i]
    elif isinstance(rhs, MonkeyNumber):
      for i in range(len(self.values)):
        ret.values[i] = (self.values[i] + rhs[i]) % MonkeyNumber.modulos[i]
    return ret

  # Same for multiplication
  def __mul__(self, rhs):
    ret = MonkeyNumber(self)
    if isinstance(rhs, int):
      for i in range(len(self.values)):
        ret.values[i] = (self.values[i] * rhs) % MonkeyNumber.modulos[i]
    elif isinstance(rhs, MonkeyNumber):
      for i in range(len(self.values)):
        ret.values[i] = (self.values[i] * rhs.values[i]) % MonkeyNumber.modulos[i]
    return ret

  # To help debugging
  def __repr__(self):
    return self.values.__repr__()

  # As we read the input, store each monkey's modulo to use for all MonkeyNumbers
  @classmethod
  def appendModulo(cls, modulo):
    cls.modulos.append(modulo)


class ThrowTest:
  def __init__(self, trueThrow, falseThrow):
    self.trueThrow = trueThrow
    self.falseThrow = falseThrow

  def decide(self, value):
    # Now each operation on a MonkeyNumber also applies each corresponding modulo,
    # so we only need to compare to 0
    if value == 0:
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
  def __init__(self, id, items, operation: Operation, test: ThrowTest):
    self.id = id
    self.rawItems = items
    self.operation = operation
    self.test = test
    self.inspections = 0

  def initItems(self):
    self.items = list(
      map(lambda rawItem: MonkeyNumber(rawItem), self.rawItems))

  def inspectItems(self):
    ret = []

    while self.items:
      self.inspections += 1
      item = self.items.pop(0)
      item = self.operation.calculate(item)
      ret.append((item, self.test.decide(item.values[self.id])))

    return ret

  def getInspections(self):
    return self.inspections

  def receiveItem(self, item):
    self.items.append(item)


while True:
  try:
    line = input()
    index = len(monkeys)
    assert (line == f'Monkey {index}:')

    startingItems = list(map(int, input().partition(': ')[2].split(',')))
    operationTokens = input().partition('new = ')[2].split()
    divisibleBy = int(input().partition('divisible by ')[2])
    trueThrow = int(input().partition('throw to monkey ')[2])
    falseThrow = int(input().partition('throw to monkey ')[2])

    operation = Operation(operationTokens)
    throwTest = ThrowTest(trueThrow, falseThrow)
    monkeys.append(Monkey(index, startingItems, operation, throwTest))

    MonkeyNumber.appendModulo(divisibleBy)

    # Empty line after each case
    input()

  except EOFError:
    break

for monkey in monkeys:
  monkey.initItems()

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
