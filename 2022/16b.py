import re
from collections import defaultdict

INFINITY = 10e23

flowRates = {}
graph = {}

totalMinutes = 26

while True:
  try:
    # Read and parse input
    line = input()
    match = re.search(r"Valve (.*) has flow rate=(.*); tunnel[s]? lead[s]? to valve[s]? (.*)", line)

    valveLabel, flowRateString, edgesString = match.groups()

    flowRates[valveLabel] = int(flowRateString)

    edges = edgesString.split(', ')
    graph[valveLabel] = edges

  except EOFError:
    break

labels = list(flowRates.keys())
minDist = [[INFINITY for _ in labels] for _ in labels]

for uLabel, edges in graph.items():
  for vLabel in edges:
    u = labels.index(uLabel)
    v = labels.index(vLabel)
    minDist[u][v] = 1

for uLabel in labels:
  u = labels.index(uLabel)
  minDist[u][u] = 1

for k in range(len(labels)):
  for i in range(len(labels)):
    for j in range(len(labels)):
      if minDist[i][j] > minDist[i][k] + minDist[k][j]:
        minDist[i][j] = minDist[i][k] + minDist[k][j]

startPoint = labels.index('AA')
totalPressure = 0

valveCombinations = defaultdict(int)

queue = []

queue.append((startPoint, totalMinutes, totalPressure, frozenset()))

while queue:
  current, timeRemaining, pressure, opened = queue.pop(0)
  valveCombinations[opened] = max(valveCombinations[opened], pressure)

  for i in range(len(labels)):
    if i not in opened and flowRates[labels[i]] > 0:
      timeTaken = minDist[current][i] + (0 if current == i else 1)

      nextTime = timeRemaining - timeTaken
      if nextTime <= 0:
        continue

      nextPressure = pressure + (flowRates[labels[i]] * nextTime)

      nextOpenedEntries = list(opened)
      nextOpenedEntries.append(i)
      nextOpened = frozenset(nextOpenedEntries)

      queue.append((i, nextTime, nextPressure, nextOpened))

# Find best combination of disjoint valve sets
bestPressure = 0

for i, iValue in valveCombinations.items():
  for j, jValue in valveCombinations.items():
    if (len(i.intersection(j)) == 0):
      bestPressure = max(bestPressure, iValue + jValue)

print(bestPressure)
