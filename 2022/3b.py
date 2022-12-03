prioritySum = 0

def priority(item):
  code = ord(item)
  if ord('A') <= code <= ord('Z'):
    return code - ord('A') + 27
  else:
    return code - ord('a') + 1

while True:
  try:
    firstBag = input()
    secondBag = input()
    thirdBag = input()

    firstBagItems = set()
    secondBagCommonItems = set()

    for i in range(len(firstBag)):
      firstBagItems.add(firstBag[i])

    for i in range(len(secondBag)):
      if secondBag[i] in firstBagItems:
        secondBagCommonItems.add(secondBag[i])

    for i in range(len(thirdBag)):
      if thirdBag[i] in secondBagCommonItems:
        prioritySum += priority(thirdBag[i])
        break

  except EOFError:
    break

print(prioritySum)

