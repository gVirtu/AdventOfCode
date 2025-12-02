import math

currentSum = 50
currentFloor = 0
currentCeil = 1
count = 0

while True:
  try:
    line = input()
    direction = line[0]
    amount = int(line[1:])

    match direction:
      case 'L':
        currentSum -= amount
      case 'R':
        currentSum += amount
        
    cycle = currentSum / 100
    nextFloor = math.floor(cycle)
    nextCeil = math.ceil(cycle)
        
    count += max(abs(nextFloor - currentFloor), abs(nextCeil - currentCeil)) - int(currentFloor == currentCeil)
    # print(f'{direction}{amount}: {currentSum} ({count})')
    currentFloor = nextFloor
    currentCeil = nextCeil

  except EOFError:
    break

print(count)
