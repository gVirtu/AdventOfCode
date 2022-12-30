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


def solve(name):
    global monkeys

    monkey = monkeys[name]

    if monkey.value is not None:
        return monkey.value
    else:
        value = operation(monkey.op, solve(monkey.lhs), solve(monkey.rhs))
        monkey.value = value
        return value


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

print(solve("root"))
