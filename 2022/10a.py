cycle = 1 # Current cycle
x = 1 # Current value of register
signalStrengthSum = 0 # Sum of signal strengths
nextCheckpoint = 20 # First check at 20th cycle
checkpointInterval = 40 # Check every 40 cycles after that

def signalStrength(cycle, x):
  return x * cycle

def processCheckpoint(cycle, x, nextCheckpoint, checkpointInterval):
  if cycle > nextCheckpoint:
    return (signalStrength(nextCheckpoint, x), nextCheckpoint + checkpointInterval)
  else:
    return (0, nextCheckpoint)

while True:
  try:
    tokens = input().split()
    command = tokens[0]

    if command == "noop":
      cycle += 1
      delta, nextCheckpoint = processCheckpoint(cycle, x, nextCheckpoint, checkpointInterval)
      signalStrengthSum += delta

    elif command == "addx":
      cycle += 2
      delta, nextCheckpoint = processCheckpoint(cycle, x, nextCheckpoint, checkpointInterval)
      signalStrengthSum += delta

      x += int(tokens[1])

  except EOFError:
    break

print(signalStrengthSum)

