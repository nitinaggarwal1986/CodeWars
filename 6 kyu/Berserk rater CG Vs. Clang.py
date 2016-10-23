def sudoku_solver(puzzle):
	
	from copy import deepcopy
	reserve = puzzle
	possibilities = []
	l = 9
	
	print(puzzle)
	
	def diagnoze(a, b, value, puzzle, ch = 1):
		p = int(a / 3)
		q = int(b / 3)
		
		if value == 0:
			return True
		
		if ch == 1:
			if puzzle[a][b] == value:
				return True
		
		for i in range(3):
			for j in range(3):
				if puzzle[3 * p + i][3 * q + j] == value and (3 * p + i != a or  3 * q + j !=  b):
					return False
				
		for y in [[a, x] for x in range(9)]:
			if puzzle[y[0]][y[1]] == value and (y[0] != a or y[1] != b):
				return False
		for y in [[x, b] for x in range(9)]:
			if puzzle[y[0]][y[1]] == value  and (y[0] != a or y[1] != b):
				return False
		return True
	
	
	if len(puzzle) != 9:
		raise RuntimeError("Invalid Puzzle")
	elif max([len(x) for x in puzzle]) != 9:
		raise RuntimeError("Invalid Puzzle")
	elif min([len(x) for x in puzzle]) != 9:
		raise RuntimeError("Invalid Puzzle")
	
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] > 9:
				raise RuntimeError("Invalid Puzzle", i, j, 1)
			elif puzzle[i][j] < 0:
				raise RuntimeError("Invalid Puzzle", i, j, 2)
			elif not diagnoze(i, j, puzzle[i][j], puzzle, 0):
				raise RuntimeError("Invalid Puzzle", i, j,puzzle[i][j], 4)
	
	def pos(a, b, puzzle):
		p = int(a / 3)
		q = int(b / 3)
		
		box = []
		for i in range(3):
			for j in range(3):
				box.append(puzzle[3 * p + i][3 * q + j])
		nbhd = [box]
		nbhd.append(puzzle[a])
		nbhd.append([x[b] for x in puzzle])
		options = list(set(list(range(1,10))) - (set(nbhd[0] + nbhd[1] + nbhd[2])))
		return options
			
	def git(a, b, posDict):	
		p = int(a / 3)
		q = int(b / 3)
		
		box = {}
		for i in range(3):
			for j in range(3):
				try:
					box[(3 * p + i, 3 * q + j)] = posDict[(3 * p + i, 3 * q + j)]
				except KeyError:
					pass
		row = {}
		column = {}
		for y in [(a, x) for x in range(9)]:
			try:
				row[y] = posDict[y]
			except KeyError:
				pass
		for y in [(x, b) for x in range(9)]:
			try:
				column[y] = posDict[y]
			except KeyError:
				pass
		
		rowd = {x : [y for y in row.keys() if x in row[y]] for x in range(1,9)}
		columnd = {x : [y for y in column.keys() if x in column[y]] for x in range(1,9)}
		boxd = {x : [y for y in box.keys() if x in box[y]] for x in range(1,9)}
		
		return [rowd, columnd, boxd]
	
	def choose(puzzle, removed):
		
		min = 9
		choices = []
		key = 0
		
		indices = indicesf(puzzle)
		
		posDict = {x : pos(x[0], x[1], puzzle) for x in indices}
		
		for x in indices:
			[row, column, box] = git(x[0], x[1], posDict)
			
			for d in [row, column, box]:
				for i in d.keys():
					if i in removed.keys() and removed[i] in d[i]:
						d[i] = [x for x in d[i] if removed[i] != x]
					if 0 < len(d[i]) < min:
						min = len(d[i])
						choices = d[i]
						key = i
						print(i, d[i], min)
		return [key, min, choices]
	
	def indicesf(puzzle):
		
		indices = []
		for i in range(9):
			for j in range(9):
				if puzzle[i][j] == 0:
					indices.append((i, j))
		return indices					
	
	def pickNsolve(puzzle, key, choice, decisions, removed):
		
		
		if diagnoze(choice[0], choice[1], key, puzzle):
			puzzle[choice[0]][choice[1]] = key
		else:
			raise RuntimeError("Puzzle undone", choice, key)
		
		indices = indicesf(puzzle)
		
		indl = len(indices) + 1
		
		puzzle1 = deepcopy(puzzle)
		
		while (len(indices) != indl):
			
			posDict = {}
			opDict = {}
			
			indices = indicesf(puzzle1)
			
			indl = len(indices)
		
			posDict = {x : pos(x[0], x[1], puzzle1) for x in indices}
			opDict = {x : len(posDict[x]) for x in posDict.keys()}
			
			for x in indices:
				[row, column, box] = git(x[0], x[1], posDict)
			
				for d in [row, column, box]:
					for i in d.keys():
						if len(d[i]) == 1:
							if puzzle1[d[i][0][0]][d[i][0][1]] == 0:
								if diagnoze(d[i][0][0], d[i][0][1], i, puzzle1):
									puzzle1[d[i][0][0]][d[i][0][1]] = i
							elif puzzle1[d[i][0][0]][d[i][0][1]] == i:
								pass
							else:
								raise RuntimeError("Puzzle undone", i, d[i])
								
			for x in posDict.keys():
				if len(posDict[x]) == 1:
					if diagnoze(x[0], x[1], posDict[x][0], puzzle1):
						puzzle1[x[0]][x[1]] = posDict[x][0]
					else:
						raise RuntimeError("Puzzle undone", x, posDict[x][0])
						
			indices = indicesf(puzzle1)
		
		if len(indices) == 0:
			return puzzle1
		
		decisions1 = deepcopy(decisions)
		decisions1[choice] = key
		
		[key1, mn1, choices1] = choose(puzzle1, removed)
		
		puzzle2 = []
		print(choices1)
		for x in choices1:
			try:
				print("For ", x, key1)
				puzzle3 = deepcopy(puzzle1)
				puzzle2.append(pickNsolve(puzzle3, key1, x, decisions1, removed))
			except RuntimeError:
				print("Removing ", x, key1)
				removed[x] = key1
				puzzle1[x[0]][x[1]] = 0
		print(puzzle2)
		if len(puzzle2) > 1:
			raise RuntimeError("Multiple Solutions", puzzle2)
		elif len(puzzle2) == 1:
			return puzzle2[0]
		else:
			raise RuntimeError("Unsolvable Puzzle")
		
	
	puzzle1 = pickNsolve(puzzle, puzzle[0][0], (0,0), {}, {})
	
	return puzzle1