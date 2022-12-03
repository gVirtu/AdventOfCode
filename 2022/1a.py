current = 0
maximum = 0

while True:
  try:
    line = input()
    if line == '':
      maximum = max(maximum, current)
      current = 0
    else:
      current += int(line)

  except EOFError:
    break

print(maximum)
