heightmap = []
bestDistance = 10e18
target = (None, None)
rowNumber = 0

queue = []

def elevation(c):
  return ord(c) - ord('a')

# Read trees
while True:
  try:
    line = input()
    row = []

    for i, character in enumerate(line):
      if character == 'S':
        start = (rowNumber, i)
        row.append(elevation('a'))
      elif character == 'E':
        target = (rowNumber, i)
        row.append(elevation('z'))
      else:
        row.append(elevation(character))

    heightmap.append(row)
    rowNumber += 1

  except EOFError:
    break

queue.append((target, 0))
rows = len(heightmap)
columns = len(heightmap[0])

class State:
  def __init__(self, heightmap, queue):
    self.heightmap = heightmap
    self.queue = queue
    self.visited = set()

state = State(heightmap, queue)

def checkElevation(state, currentPos, nextPos, nextDistance):
  currentElevation = state.heightmap[currentPos[0]][currentPos[1]]
  nextElevation = state.heightmap[nextPos[0]][nextPos[1]]

  if nextPos not in state.visited and (currentElevation - nextElevation) <= 1:
    state.visited.add(nextPos)
    state.queue.append((nextPos, nextDistance))

while queue:
  position, distance = queue.pop(0)
  currentElevation = heightmap[position[0]][position[1]]

  if currentElevation == elevation('a'):
    bestDistance = min(bestDistance, distance)
    break

  if position[0] > 0:
    checkElevation(state, position, (position[0] - 1, position[1]), distance + 1)
  if position[1] > 0:
    checkElevation(state, position, (position[0], position[1] - 1), distance + 1)
  if position[0] < rows - 1:
    checkElevation(state, position, (position[0] + 1, position[1]), distance + 1)
  if position[1] < columns - 1:
    checkElevation(state, position, (position[0], position[1] + 1), distance + 1)

print(bestDistance)
