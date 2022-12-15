cave = []
rockLines = []

sourcePos = (500, 0)

width = sourcePos[0] + 1
height = sourcePos[1] + 1

paddingRight = 500
paddingBottom = 2

totalSand = 0

AIR = '⬛'
WALL = '⬜'
SOURCE = '🐇'
SAND = '🐰'


def printCave(cave):
  for row in cave:
    print(''.join(row))
  print('')



def hasWall(cave, point):
  return cave[point[1]][point[0]] in [WALL, SAND]


def spawnSand(cave, point, fallen=False):
  # Fall directly down, diagonally left or diagonally right
  targets = [
    (point[0], point[1] + 1),
    (point[0] - 1, point[1] + 1),
    (point[0] + 1, point[1] + 1)
  ]

  for target in targets:
    if not hasWall(cave, target):
      return spawnSand(cave, target, True)

  if (cave[point[1]][point[0]] == SOURCE):
    return False

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

    rockLines.append(line)

  except EOFError:
    break

# Allocate cave

width += paddingRight
height += paddingBottom

cave = [[AIR for _ in range(width)] for _ in range(height)]

# Position sand source

cave[sourcePos[1]][sourcePos[0]] = SOURCE

# Create rocks

for line in rockLines:
  prevPoint = line.pop(0)

  while line:
    nextPoint = line.pop(0)

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

# Create floor

for i in range(width):
  cave[-1][i] = WALL

# Create sand
while True:
  totalSand += 1
  if spawnSand(cave, sourcePos):
    pass
  else:
    break

printCave(cave)
print(totalSand)

