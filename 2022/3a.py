prioritySum = 0

def priority(item):
  code = ord(item)
  if ord('A') <= code <= ord('Z'):
    return code - ord('A') + 27
  else:
    return code - ord('a') + 1

while True:
  try:
    line = input()

    compartmentSize = len(line) // 2

    firstCompartment = line[:compartmentSize]
    secondCompartment = line[compartmentSize:]

    firstCompartmentItems = set()

    for i in range(compartmentSize):
      firstCompartmentItems.add(firstCompartment[i])

    for i in range(compartmentSize):
      if secondCompartment[i] in firstCompartmentItems:
        prioritySum += priority(secondCompartment[i])
        break

  except EOFError:
    break

print(prioritySum)
