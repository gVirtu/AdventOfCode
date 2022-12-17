import re

sensorDistances = []
targetRow = 2000000
targetRowBeacons = set()

def manhattan(x, y):
  return abs(x[0] - y[0]) + abs(x[1] - y[1])

while True:
  try:
    # Read and parse input
    line = input()
    match = re.findall(r"x=([\-0-9]+), y=([\-0-9]+)", line)

    sensor, beacon = map(lambda t: (int(t[0]), int(t[1])), match)

    # Calculate sensor's covered radius
    distance = manhattan(sensor, beacon)
    sensorDistances.append((sensor, distance))

    # Save beacons that are in our target row to exclude from result
    if (beacon[1] == targetRow):
      targetRowBeacons.add(beacon)

  except EOFError:
    break

ranges = []

for checkIndex in range(len(sensorDistances)):
  sensor, radius = sensorDistances[checkIndex]
  checkIndex += 1

  # By checking how far each sensor is to the target row in the Y direction,
  # we know how many cells its coverage spans in the target row (= amplitude)
  loss = abs(targetRow - sensor[1])
  amplitude = radius - loss

  if (amplitude < 0):
    continue

  # Each range is a contiguous line in the X axis that is covered by this sensor
  rangeStart = sensor[0] - amplitude
  rangeEnd = sensor[0] + amplitude

  ranges.append((rangeStart, rangeEnd))

# Now we merge overlapping ranges
ranges.sort()
mergeIndex = 0

for i in range(1, len(ranges)):
  if (ranges[mergeIndex][1] >= ranges[i][0]):
    ranges[mergeIndex] = (ranges[mergeIndex][0], max(ranges[mergeIndex][1], ranges[i][1]))
  else:
    mergeIndex += 1
    ranges[mergeIndex] = ranges[i]

ranges = ranges[:mergeIndex+1]

# Lastly, sum up each merged range size to calculate coverage,
# subtracting by one for each beacon that is inside any of the ranges

beaconList = list(targetRowBeacons)
beaconList.sort()

beaconIndex = 0

coverage = 0
for range in ranges:
  coverage += range[1] - range[0] + 1

  while beaconIndex < len(beaconList) and beaconList[beaconIndex][0] <= range[1]:
    if beaconList[beaconIndex][0] >= range[0]:
      coverage -= 1

    beaconIndex += 1

print(coverage)
