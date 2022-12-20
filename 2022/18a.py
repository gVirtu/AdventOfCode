coords = set()

while True:
  try:
    line = input()
    x, y, z = map(int, line.split(','))
    coords.add((x, y, z))

  except EOFError:
    break

count = 0

for (x, y, z) in coords:
  count += 0 if (x + 1, y, z) in coords else 1
  count += 0 if (x - 1, y, z) in coords else 1
  count += 0 if (x, y + 1, z) in coords else 1
  count += 0 if (x, y - 1, z) in coords else 1
  count += 0 if (x, y, z + 1) in coords else 1
  count += 0 if (x, y, z - 1) in coords else 1

print(count)
