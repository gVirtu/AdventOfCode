treeHeights = [] # Height of each tree
treeMaxHeights = [] # Store max height 'seen' by each tree vertically and horizontally
treeVisible = [] # Whether tree is visible by some side

# Read trees
while True:
  try:
    line = input()
    treeHeights.append(list(map(int, line)))
    treeMaxHeights.append([[-1, -1] for _ in range(len(line))])
    treeVisible.append([False for _ in range(len(line))])

  except EOFError:
    break

rows = len(treeHeights)
columns = len(treeHeights[0])

# Mark corners
for i in range(rows):
  treeVisible[i][0] = True
  treeVisible[i][columns - 1] = True

for j in range(columns):
  treeVisible[0][j] = True
  treeVisible[rows - 1][j] = True


# First pass: Top-left to bottom-right
for i in range(1, len(treeHeights)):
  for j in range(1, len(treeHeights[i])):
    treeMaxHeights[i][j][0] = max(treeMaxHeights[i - 1][j][0], treeHeights[i - 1][j])
    treeMaxHeights[i][j][1] = max(treeMaxHeights[i][j - 1][1], treeHeights[i][j - 1])

    treeVisible[i][j] = treeVisible[i][j] or (treeHeights[i][j] > treeMaxHeights[i][j][0]) or (treeHeights[i][j] > treeMaxHeights[i][j][1])

# Reset max heights before second pass
treeMaxHeights = [
  [[-1, -1] for _ in range(columns)]
    for _ in range(rows)
]

# Second pass: Bottom-right to top-left
for i in range(len(treeHeights)-2, -1, -1):
  for j in range(len(treeHeights[i])-2, -1, -1):
    treeMaxHeights[i][j][0] = max(treeMaxHeights[i + 1][j][0], treeHeights[i + 1][j])
    treeMaxHeights[i][j][1] = max(treeMaxHeights[i][j + 1][1], treeHeights[i][j + 1])

    treeVisible[i][j] = treeVisible[i][j] or (treeHeights[i][j] > treeMaxHeights[i][j][0]) or (treeHeights[i][j] > treeMaxHeights[i][j][1])

print(sum(sum(row) for row in treeVisible))

