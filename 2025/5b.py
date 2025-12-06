fresh_ranges = []
merged_ranges = []
fresh_count = 0

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

for r in merged_ranges:
  fresh_count += r[1]-r[0]+1
  
print(fresh_count)