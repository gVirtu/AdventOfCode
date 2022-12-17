import re

minCoord = 0
maxCoord = 4000000

excludeRanges = [
  [] for _ in range(maxCoord + 1)
]

def manhattan(x, y):
  return abs(x[0] - y[0]) + abs(x[1] - y[1])

def appendExcludeRange(row, startX, endX):
  global excludeRanges

  if row < minCoord or row > maxCoord or startX > maxCoord or endX < minCoord:
    return

  excludeRanges[row].append((max(minCoord, startX), min(maxCoord, endX)))

def mergeRanges(ranges):
  ranges.sort()
  mergeIndex = 0

  for i in range(1, len(ranges)):
    if (ranges[mergeIndex][1] >= ranges[i][0] - 1):
      ranges[mergeIndex] = (ranges[mergeIndex][0], max(ranges[mergeIndex][1], ranges[i][1]))
    else:
      mergeIndex += 1
      ranges[mergeIndex] = ranges[i]

  return ranges[:mergeIndex+1]

def tuningFrequency(x, y):
  return x * 4000000 + y

while True:
  try:
    # Read and parse input
    line = input()
    match = re.findall(r"x=([\-0-9]+), y=([\-0-9]+)", line)

    sensor, beacon = map(lambda t: (int(t[0]), int(t[1])), match)

    # Calculate sensor's covered radius
    distance = manhattan(sensor, beacon)

    appendExcludeRange(sensor[1], sensor[0] - distance, sensor[0] + distance)

    for i in range(1, distance + 1):
      appendExcludeRange(sensor[1] - i, sensor[0] - (distance - i), sensor[0] + (distance - i))
      appendExcludeRange(sensor[1] + i, sensor[0] - (distance - i), sensor[0] + (distance - i))

  except EOFError:
    break

# Check excludeRanges that, when merged, contain the whole search space
# When we find the first one that does not, return it

for i, er in enumerate(excludeRanges):
  merged = mergeRanges(er)

  if len(merged) == 2:
    print(tuningFrequency(merged[0][1] + 1, i))
    break
