grid = []

def count_neighbors(r: int, c: int):
  neighbors = 0

  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i == 0 and j == 0):
        continue
      neighbors += int(grid[r+i][c+j] == '@')
      
  # print(f'grid[{r}][{c}] has {neighbors} neighbors')
  return neighbors

while True:
  try:
    line = input()
    grid.append(list(line))

  except EOFError:
    break

rows = len(grid)
cols = len(grid[0])

row_padding = ['.'] * (cols + 2)

for i in range(0, rows):
  grid[i].insert(0, '.')
  grid[i].append('.')

grid.insert(0, row_padding)
grid.append(row_padding)

total = 0

for i in range(1, rows + 1):
  for j in range(1, cols + 1):
    total += int(grid[i][j] == '@' and count_neighbors(i, j) < 4)

print(total)

