currentSum = 50
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
      
    count += int(currentSum % 100 == 0)

  except EOFError:
    break

print(count)
