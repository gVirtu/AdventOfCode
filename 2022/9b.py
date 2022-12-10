ropeSize = 10
rope = [(0, 0) for _ in range(ropeSize)]
tailCoordSet = set([rope[-1]])

moveDelta = {
  'U': lambda x: (-x, 0),
  'L': lambda x: (0, -x),
  'D': lambda x: (x, 0),
  'R': lambda x: (0, x),
}


def move(coords, direction, distance):
  delta = moveDelta[direction](distance)
  return tuple(coords[i] + delta[i] for i in range(2))


def coordDistance(nodeA, nodeB):
  delta_x = abs(nodeA[0] - nodeB[0])
  delta_y = abs(nodeA[1] - nodeB[1])
  return delta_x + delta_y - min(delta_x, delta_y)


def catchUp(head, tail):
  if coordDistance(head, tail) > 1:
    if (tail[0] != head[0]):
      delta = 1 if head[0] > tail[0] else -1
      tail = (tail[0] + delta, tail[1])
    if (tail[1] != head[1]):
      delta = 1 if head[1] > tail[1] else -1
      tail = (tail[0], tail[1] + delta)

  return tail


while True:
  try:
    direction, distance = input().split()

    for i in range(int(distance)):
      rope[0] = move(rope[0], direction, 1)
      for i in range(1, len(rope)):
        rope[i] = catchUp(rope[i-1], rope[i])

      tailCoordSet.add(rope[-1])

  except EOFError:
    break

print(len(tailCoordSet))
