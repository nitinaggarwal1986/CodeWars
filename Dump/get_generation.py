def get_generation(cells, generations):
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
    
	def weight(ind, space):
		
		#global space
		
		indices = []
		
		for i in range(-1, 2):
			for j in range(-1, 2):
				indices.append((ind[0] + i, ind[1] + j))
		
		count = 0
		
		for x in indices:
			if x in space.keys() and x != ind:
				count += space[x]
		
		return [count, indices]
	
	def dictArr(dict):
		
		x = set([x[0] for x in dict.keys() if dict[x] != 0])
		y = set([x[1] for x in dict.keys() if dict[x] != 0])
		
		l, m = min(x), max(x)
		p, q = min(y), max(y)
		
		temp = []
		
		for i in range(l, m + 1):
			temp.append([])
			for j in range(p, q + 1):
				temp[-1].append(dict[(i, j)])
		
		return temp
		
	iter = list(space.keys())
	print(iter)
	
	for s in range(generations + 1):
		tspace = {}
		for x in iter:
			[count, indices] = weight(x, space)
		
			for i in indices:
				if i not in space.keys():
					space[i] = 0
		iter = list(space.keys())
		
		for x in iter:
			[count, indices] = weight(x, space)
			
			if (count, space[x]) in rules.keys():
				tr = rules[(count, space[x])]
				print(x, (count, space[x]), tr)
				tspace[x] = tr
			print(htmlize(dictArr(space)))
			
		for x in tspace.keys():
			space[x] = tspace[x]
	
	return dictArr(space)