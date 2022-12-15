cave = []
rockLines = []

width = 501
height = 1

offsetX = 10e18
offsetY = 0

sourcePos = (500, 0)
totalSand = 0

AIR = '⬛'
WALL = '⬜'
SOURCE = '🐇'
SAND = '🐰'


def normalize(point):
  global offsetX, offsetY
  return (point[0] - offsetX, point[1] - offsetY)


def printCave(cave):
  for row in cave:
    print(''.join(row))
  print('')


def inBounds(point):
  global width, height

  return point[0] >= 0 \
      and point[1] < height \
      and point[0] < width


def hasWall(cave, point):
  return inBounds(point) and cave[point[1]][point[0]] in [WALL, SAND]


def spawnSand(cave, point):
  # Fall directly down, diagonally left or diagonally right
  targets = [
    (point[0], point[1] + 1),
    (point[0] - 1, point[1] + 1),
    (point[0] + 1, point[1] + 1)
  ]

  for target in targets:
    if not hasWall(cave, target):
      if not inBounds(target):
        return False
      return spawnSand(cave, target)

  cave[point[1]][point[0]] = SAND
  return True


# Read input

while True:
  try:
    line = list(
      map(lambda x: tuple(map(int, x.split(','))), input().split(' -> ')))

    for coords in line:
      width = max(width, coords[0] + 1)
      height = max(height, coords[1] + 1)
      offsetX = min(offsetX, coords[0])
      offsetY = min(offsetY, coords[1])

    rockLines.append(line)

  except EOFError:
    break

# Allocate cave

width -= offsetX
height -= offsetY

cave = [[AIR for _ in range(width)] for _ in range(height)]

# Position sand source

sourcePos = normalize(sourcePos)
cave[sourcePos[1]][sourcePos[0]] = SOURCE

# Create rocks

for line in rockLines:
  prevPoint = normalize(line.pop(0))

  while line:
    nextPoint = normalize(line.pop(0))

    if prevPoint[0] == nextPoint[0]:
      j = prevPoint[0]
      step = 1 if nextPoint[1] > prevPoint[1] else -1

      for i in range(prevPoint[1], nextPoint[1] + step, step):

        cave[i][j] = WALL

    if prevPoint[1] == nextPoint[1]:
      i = prevPoint[1]
      step = 1 if nextPoint[0] > prevPoint[0] else -1

      for j in range(prevPoint[0], nextPoint[0] + step, step):
        cave[i][j] = WALL

    prevPoint = nextPoint

# Create sand
while True:
  if spawnSand(cave, sourcePos):
    totalSand += 1
  else:
    break

printCave(cave)
print(totalSand)
