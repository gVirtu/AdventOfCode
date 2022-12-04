fullyContainedCount = 0

def isFullyContained(a, b):
  return a[0] <= b[0] and a[1] >= b[1]

while True:
  try:
    line = input()
    aString, bString = line.split(',')

    a = tuple(map(int, aString.split('-')))
    b = tuple(map(int, bString.split('-')))

    if isFullyContained(a, b) or isFullyContained(b, a):
      fullyContainedCount += 1

  except EOFError:
    break

print(fullyContainedCount)

