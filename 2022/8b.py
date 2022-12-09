import math

treeHeights = [] # Height of each tree
treeSightLimit = [] # Store index of max height 'seen' by each tree vertically and horizontally
treeScore = [] # For each tree, store number of trees seen in each direction

# Read trees
while True:
  try:
    line = input()
    treeHeights.append(list(map(int, line)))
    treeSightLimit.append([[0, 0] for _ in range(len(line))])
    treeScore.append([[0, 0, 0, 0] for _ in range(len(line))])

  except EOFError:
    break

rows = len(treeHeights)
columns = len(treeHeights[0])

def getVerticalSightLimit(i, j, target):
  if target <= 0 or target >= rows-1:
    return min(max(0, target), rows-1)

  if treeHeights[i][j] > treeHeights[target][j]:
    return getVerticalSightLimit(i, j, treeSightLimit[target][j][0])
  else:
    return target

def getHorizontalSightLimit(i, j, target):
  if target <= 0 or target >= columns-1:
    return min(max(0, target), columns-1)

  if treeHeights[i][j] > treeHeights[i][target]:
    return getHorizontalSightLimit(i, j, treeSightLimit[i][target][1])
  else:
    return target

# First pass: Top-left to bottom-right
for i in range(len(treeHeights)):
  for j in range(len(treeHeights[i])):
    treeSightLimit[i][j] = [
      getVerticalSightLimit(i, j, i - 1),
      getHorizontalSightLimit(i, j, j - 1)
    ]

    treeScore[i][j][0] = i - treeSightLimit[i][j][0]
    treeScore[i][j][1] = j - treeSightLimit[i][j][1]

# Reset sight limit before second pass
treeSightLimit = [
  [[rows-1, columns-1] for _ in range(columns)]
    for _ in range(rows)
]

# Second pass: Bottom-right to top-left
for i in range(len(treeHeights)-1, -1, -1):
  for j in range(len(treeHeights[i])-1, -1, -1):
    treeSightLimit[i][j] = [
      getVerticalSightLimit(i, j, i + 1),
      getHorizontalSightLimit(i, j, j + 1)
    ]

    treeScore[i][j][2] = treeSightLimit[i][j][0] - i
    treeScore[i][j][3] = treeSightLimit[i][j][1] - j

scoreList = [math.prod(scores) for row in treeScore for scores in row]
print(max(scoreList))
