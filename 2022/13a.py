packetIndex = 1
rightOrderSum = 0

def compare(left, right):
  if isinstance(left, int) and isinstance(right, int):
    if left < right:
      return True
    elif right < left:
      return False
    else:
      return None

  if isinstance(left, list) and isinstance(right, list):
    minLen = min(len(left), len(right))

    for i in range(minLen):
      result = compare(left[i], right[i])
      if result is not None:
        return result

    if len(left) < len(right):
      return True
    elif len(right) < len(left):
      return False
    else:
      return None

  if isinstance(left, int):
    return compare([left], right)
  else:
    return compare(left, [right])

while True:
  try:
    leftPacket = eval(input()) # Shortcut to read the lists
    rightPacket = eval(input()) # do not try this at home

    if compare(leftPacket, rightPacket):
      rightOrderSum += packetIndex

    # Empty line between tests
    input()

    packetIndex += 1

  except EOFError:
    break

print(rightOrderSum)
