coords = set()
exterior = set()

maxX = 0
maxY = 0
maxZ = 0

while True:
  try:
    line = input()
    x, y, z = map(int, line.split(','))

    coords.add((x, y, z))
    maxX = max(x, maxX)
    maxY = max(y, maxY)
    maxZ = max(z, maxZ)

  except EOFError:
    break

def checkCoord(coord, exterior):
  global maxX, maxY, maxZ, coords
  x, y, z = coord

  if coord in exterior or x in [0, maxX + 1] or y in [0, maxY + 1] or z in [0, maxZ + 1]:
    return 1

  return 0

def surfaceArea(coords, exterior):
  count = 0

  for (x, y, z) in coords:
    count += checkCoord((x + 1, y, z), exterior)
    count += checkCoord((x - 1, y, z), exterior)
    count += checkCoord((x, y + 1, z), exterior)
    count += checkCoord((x, y - 1, z), exterior)
    count += checkCoord((x, y, z + 1), exterior)
    count += checkCoord((x, y, z - 1), exterior)

  return count

def visit(visited:set, x, y, z):
  global maxX, maxY, maxZ, coords, exterior
  visited.add((x, y, z))

  if ((x, y, z) in coords):
    return False

  if ((x, y, z)) in exterior:
    return True

  if (x in [0, maxX] or y in [0, maxY] or z in [0, maxZ]):
    exterior.add((x, y, z))
    return True

  for dx, dy, dz in [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1],
  ]:
    nextPos = (x + dx, y + dy, z + dz)
    if (nextPos not in visited and visit(visited, *nextPos)):
      exterior.add((x, y, z))
      return True

  return False

for i in range(maxX + 1):
  for j in range(maxY + 1):
    for k in range(maxZ + 1):
      if (i, j, k) in coords:
        continue

      visited = set()
      if visit(visited, i, j, k):
        exterior.add((i, j, k))

print(surfaceArea(coords, exterior))
