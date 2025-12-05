total = 0

def find_max(battery: str, acc: str, start: int, remaining: int):
  if remaining == 0:
      return int(acc)
  
  end = len(battery) - remaining + 1
  max_in_range = 0
  best = 0
  
  for i in range(start, end):
    max_in_range = max(max_in_range, ord(battery[i]) - ord('0'))
    
  for i in range(start, end):
    if (ord(battery[i]) - ord('0')) == max_in_range:
      best = max(best, find_max(battery, acc + battery[i], i + 1, remaining - 1))
      
  return best


while True:
  try:
    line = input()
    
    res = find_max(line, '', 0, 12)
    
    # print(res)
    
    total += res

  except EOFError:
    break

print(total)

