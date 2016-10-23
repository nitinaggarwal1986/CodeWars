def spiralize(size):
  board = []
  if size == 0:
    return []
  for i in range(size):
    board.append([])
    for j in range(size):
      board[i].append(0)
  board[0][0] = 1
  loop = size * (size - 1)
  flip = 0
  ind = 0
  min = 0
  max = size
  other = 0
  x = 0
  y = 0
  for i in range(loop):
    if max - min == 1:
      break
    ind = i % 2
    flip = int(i / 2) % 2
    if ind:
      other = y
    else:
      other = x
    
    if ind:
      if flip:
        max = size - int((i + 1) / 2) 
      else:
        min = int((i + 1) / 2)
    
    for j in range(min, max):
      f = (1 - flip) * j + flip * (size - j - 1)
      x = (1 - ind) * other + ind * f
      y = ind * other + (1 - ind) * f
      board[x][y] = 1
  return board