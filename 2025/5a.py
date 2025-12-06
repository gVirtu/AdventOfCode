fresh_ranges = []
merged_ranges = []
fresh_count = 0

def search_id(id: int, st: int, en: int):
  # print(f'ID {id} ST={st} EN={en}')
  if (en < st):
    return False

  mid = st+(en-st)//2

  if (merged_ranges[mid][0] <= id <= merged_ranges[mid][1]):
    return True
  elif (id < merged_ranges[mid][0]):
    # print('BRANCH LEFT')
    return search_id(id, st, mid - 1)
  else:
    # print('BRANCH RIGHT')
    return search_id(id, mid + 1, en)


while True:
  try:
    line = input()
    if (len(line) == 0):
      break
    
    fresh_ranges.append(list(map(int, line.split('-'))))

  except EOFError:
    break
  
fresh_ranges.sort()

# Merge ranges
last_range = fresh_ranges[0]

for i in range(1, len(fresh_ranges)):
  current_range = fresh_ranges[i]
  
  if current_range[1] < last_range[1]:
    continue
  elif current_range[0] <= last_range[1]:
    last_range[1] = current_range[1]
  else:
    merged_ranges.append(last_range)
    last_range = current_range

merged_ranges.append(last_range)

merged_range_count = len(merged_ranges)

while True:
  try:
    line = input()

    if search_id(int(line), 0, merged_range_count - 1):
      # print(f'ID {line} is fresh!')
      fresh_count += 1

  except EOFError:
    break
  
print(fresh_count)
