cycle = 0 # Current cycle
x = 1 # Current value of register
nextX = 1 # Next value of register
nextXCycle = 0 # Cycle after the current operation finishes
screenColumns = 40

while True:
  try:
    tokens = input().split()
    command = tokens[0]

    if command == "noop":
      nextXCycle += 1
      nextX = x

    elif command == "addx":
      nextXCycle += 2
      nextX = x + int(tokens[1])

    while cycle < nextXCycle:
      lit = abs(x - (cycle%screenColumns)) <= 1

      pixel = '#' if lit else '.'
      print(pixel, end='')

      if (cycle and (cycle+1) % screenColumns == 0):
        print('')

      cycle += 1

    x = nextX

  except EOFError:
    break
