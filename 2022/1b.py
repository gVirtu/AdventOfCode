import heapq

current = 0
capacity = 3
heap = []

def addElf():
  heapq.heappush(heap, current)

  if (len(heap) > capacity):
    popped = heapq.heappop(heap)

while True:
  try:
    line = input()
    if line == '':
      addElf()
      current = 0
    else:
      current += int(line)

  except EOFError:
    addElf()
    break

print(sum(heap))
