grid = []
neighbor_count = {}
to_remove = set()
removed = 0

def count_neighbors(r: int, c: int):
  neighbors = 0

  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i == 0 and j == 0):
        continue
      neighbors += int(grid[r+i][c+j] == '@')
      
  # print(f'grid[{r}][{c}] has {neighbors} neighbors')
  return neighbors


def decrement_neighbors(coords: tuple):
  (r, c) = coords

  for i in range(-1, 2):
    for j in range(-1, 2):
      coords = (r+i, c+j)
      if ((i != 0 or j != 0) and coords in neighbor_count):
        neighbor_count[coords] -= 1
        if neighbor_count[coords] < 4:
          # print(f'Neighbor {coords} queued for removal')
          to_remove.add(coords)
          del neighbor_count[coords]


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
    if (grid[i][j] == '@'):
      count = count_neighbors(i, j)
      if count < 4:
        to_remove.add((i, j))
      else:
        neighbor_count[(i, j)] = count
        

# print(neighbor_count)
pass_i = 1

while(len(to_remove)):
  # print(f'PASS #{pass_i} - {len(to_remove)} rolls to be removed')

  removed += len(to_remove)
  removed_rolls = list(to_remove)
  to_remove = set()
  
  for coords in removed_rolls:
    # print(f'Removing {coords}')
    decrement_neighbors(coords)
    
  pass_i += 1


print(removed)

