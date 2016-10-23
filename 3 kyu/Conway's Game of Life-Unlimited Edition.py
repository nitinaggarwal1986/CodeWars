def get_generation(cells, generations):
  print(cells)
  space = {}
  for i in range(len(cells)):
    for j in range(len(cells[0])):
      space[(i, j)] = cells[i][j]
  
  rules = {
    (0, 1) : 0,
    (1, 1) : 0, 
    (2, 1) : 1,
    (3, 1) : 1,
    (3, 0) : 1,
    (4, 1) : 0,
    (5, 1) : 0,
    (6, 1) : 0,
    (7, 1) : 0,
    (8, 1) : 0
  }
    
  def indices(ind):
    indices1 = []
    
    for i in range(-1, 2):
      for j in range(-1, 2):
        indices1.append((ind[0] + i, ind[1] + j))
    
    return indices1
  def weight(ind, space):
    
    #global space
    #print([(x, space[x]) for x in space if space[x]==1])
    indices1 = indices(ind) 
    
    count = 0
    
    for x in indices1:
      if x in space.keys() and x != ind:
        count += space[x]
    
    return count
  
  def dictArr(dict):
    if len([x for x in dict.keys() if dict[x] == 1]) == 0:
      return [[]]
    e = [x[0] for x in dict.keys() if dict[x] == 1]
    f = [x[1] for x in dict.keys() if dict[x] == 1]
    
    l = min(e)
    m = max(e)
    p = min(f)
    q = max(f)
    temp = []
    
    for i in range(0, m - l + 1):
      temp.append([])
      for j in range(0, q - p + 1):
        if (i + l, j + p) in dict.keys():
          temp[i].append(dict[(i + l, j + p)])
        else:
          temp[i].append(0)
    
    return temp
  
  
  iter = list(space.keys())
  print(generations)
  for s in range(generations if generations < 16 else 16):
    
    for x in iter:
      indices1 = indices(x)
    
      for i in indices1:
        if i not in space.keys():
          space[i] = 0
    
    iter = list(space.keys())
    temp = {}
    for x in iter:
      count = weight(x, space)
      if (count, space[x]) in rules.keys():
        tr = rules[(count, space[x])]
        temp[x] = tr
    for x in temp.keys():
      space[x] = temp[x]
    
    space = {x : space[x] for x in space.keys() if space[x] == 1}
    
  return dictArr(space)