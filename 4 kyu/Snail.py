def snail(array):
  print(array)
  if array == [[]]:
    return []
  elif len(array) == 1:
    return array[0]
  
  size = len(array)
  loop = size * (size - 1)
  print(size)
  flip = 0
  ind = 0
  min = 0
  max = size
  other = 0
  x = 0
  y = 0
  result = []
  for i in range(loop + 2):
    if len(result) == size * size:
      break
    ind = i % 2
    flip = int(i / 2) % 2
    if ind:
      other = y
    else:
      other = x
    
    if ind:
      if flip:
        max = max - 1 
      else:
        min = min + 1
    
    for j in range(min, max):
      f = (1 - flip) * j + flip * (size - j - 1)
      x = (1 - ind) * other + ind * f
      y = ind * other + (1 - ind) * f
      if 0 <= x < size and 0 <= y < size:
        result.append(array[x][y])
    
  return result