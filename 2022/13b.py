import functools

firstDivider = [[2]]
secondDivider = [[6]]
packets = []

def compare(left, right):
  if isinstance(left, int) and isinstance(right, int):
    if left < right:
      return -1
    elif right < left:
      return 1
    else:
      return 0

  if isinstance(left, list) and isinstance(right, list):
    minLen = min(len(left), len(right))

    for i in range(minLen):
      result = compare(left[i], right[i])
      if result != 0:
        return result

    if len(left) < len(right):
      return -1
    elif len(right) < len(left):
      return 1
    else:
      return 0

  if isinstance(left, int):
    return compare([left], right)
  else:
    return compare(left, [right])

while True:
  try:
    leftPacket = eval(input()) # Shortcut to read the lists
    rightPacket = eval(input()) # do not try this at home

    packets.append(leftPacket)
    packets.append(rightPacket)

    # Empty line between tests
    input()

  except EOFError:
    break

packets.append(firstDivider)
packets.append(secondDivider)

packets.sort(key=functools.cmp_to_key(compare))

firstDividerPos = packets.index(firstDivider) + 1
secondDividerPos = packets.index(secondDivider) + 1

print(firstDividerPos * secondDividerPos)
