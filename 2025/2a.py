count = 0

def process_range(start: str, end: str):
  # print(f'Processing {start}-{end}')

  start_len = len(start)
  end_len = len(end)

  minimum_half: str = start[:start_len//2] if (start_len % 2 == 0) else str(10**(start_len//2))

  if (int(start) > int(minimum_half*2)):
    minimum_half = str(int(minimum_half)+1) 
    
  # minimum = minimum_half*2
  
  maximum_half: str = end[:end_len//2] if (end_len % 2 == 0) else str((10**(end_len//2))-1)
  
  if (int(end) < int(maximum_half*2)):
    maximum_half = str(int(maximum_half)-1) 

  # maximum = maximum_half*2

  id_sum = 0
  
  for i in range(int(minimum_half), int(maximum_half) + 1):
    id_sum += int(str(i)*2)

  # print({'minimum': minimum_half, 'maximum': maximum_half, 'id_sum': id_sum})

  return id_sum

line = input()
range_strings = line.split(',')

for range_string in range_strings:
  [st, en] = range_string.split('-')
  
  count += process_range(st, en)

print(count)
