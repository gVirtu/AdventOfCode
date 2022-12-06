import re

stackCount = 0
stacks = []

inputLines = []


def isCrateLine(line):
  return "[" in line or "]" in line


def buildStacks():
  for i in range(stackCount):
    stacks.append([])

  while inputLines:
    inputLine = inputLines.pop()

    for i in range(stackCount):
      crate = inputLine[i * 4 + 1]

      if crate != " ":
        stacks[i].append(crate)


def executeCommand(command):
  match = re.search(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)", command)

  count, source, target = map(int, match.groups())

  crates = []

  for i in range(count):
    crates.append(stacks[source - 1].pop())

  while crates:
    stacks[target - 1].append(crates.pop())


# Read crates
while True:
  try:
    line = input()

    if isCrateLine(line):
      inputLines.append(line)
    else:
      # Line with crate indices
      stackCount = len(line.split())
      buildStacks()
      break

  except EOFError:
    break

# Empty line between crates and commands
input()

# Read commands
while True:
  try:
    line = input()
    executeCommand(line)

  except EOFError:
    break

print("".join(stack[-1] for stack in stacks))
