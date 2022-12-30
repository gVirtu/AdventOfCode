monkeys = {}


class Monkey:
    def __init__(self, value, lhs, op, rhs) -> None:
        self.value = value
        self.lhs = lhs
        self.op = op
        self.rhs = rhs

    def __repr__(self):
        if self.value is None:
            return f"{self.lhs} {self.op} {self.rhs}"
        return f"{self.value}"


def operation(op, lhs, rhs):
    return {
        "+": (lambda lhs, rhs: lhs + rhs),
        "-": (lambda lhs, rhs: lhs - rhs),
        "*": (lambda lhs, rhs: lhs * rhs),
        "/": (lambda lhs, rhs: lhs / rhs),
    }[op](lhs, rhs)


def reverseOperation(op, operand, side, result):
    return {
        "+": (lambda operand, _, result: result - operand),
        "-": (
            lambda operand, side, result: (result + operand)
            if side == "left"
            else (-result + operand)
        ),
        "*": (lambda operand, _, result: result / operand),
        "/": (
            lambda operand, side, result: (result * operand)
            if side == "left"
            else (operand / result)
        ),
    }[op](operand, side, result)


def printOperation(op, operand, side, result):
    if side == "left":
        print(f"x {op} {operand} = {result}")
    elif side == "right":
        print(f"{operand} {op} x = {result}")


def solve(name):
    global monkeys

    monkey = monkeys[name]

    if monkey.value is not None:
        return monkey.value
    else:
        value = operation(monkey.op, solve(monkey.lhs), solve(monkey.rhs))
        monkey.value = value
        return value


def findHuman(name) -> list[tuple] | None:
    global monkeys

    if name is None:
        return None
    elif name == "humn":
        return []
    else:
        monkey = monkeys[name]
        left = findHuman(monkey.lhs)
        if left is not None:
            left.append((monkey.op, monkeys[monkey.rhs].value, "left"))
            return left

        right = findHuman(monkey.rhs)
        if right is not None:
            right.append((monkey.op, monkeys[monkey.lhs].value, "right"))
            return right

        return None


while True:
    try:
        line = input()

        monkeyName, _, monkeyExpr = line.partition(": ")
        monkeyValue = None
        monkeyLhs = None
        monkeyOp = None
        monkeyRhs = None

        try:
            monkeyValue = int(monkeyExpr)
        except ValueError:
            monkeyLhs, monkeyOp, monkeyRhs = monkeyExpr.split(" ")

        monkeys[monkeyName] = Monkey(
            value=monkeyValue, lhs=monkeyLhs, op=monkeyOp, rhs=monkeyRhs
        )

    except EOFError:
        break

# Populate monkey values
solve("root")

# Assumption: human is only referenced once in either LHS or RHS of the root
opStack = findHuman("root")

assert opStack is not None

# The last element will be the known side of the root
_, expectedValue, _ = opStack.pop()

for op, value, side in reversed(opStack):
    # printOperation(op, value, side, expectedValue)
    expectedValue = reverseOperation(op, value, side, expectedValue)
    # print(f"x must be {expectedValue}")


print(expectedValue)
