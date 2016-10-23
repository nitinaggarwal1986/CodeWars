def sudoku(puzzle):
	
	reserve = puzzle
	possibilities = []
	l = 9
	
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
	
	indices = []
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] == 0:
				indices.append((i, j))
	
	while (len(indices) > 0):
		
		posDict = {}
		opDict = {}
		
		posDict = {x : pos(x[0], x[1], puzzle) for x in indices}
		opDict = {x : len(posDict[x]) for x in posDict.keys()}
		for x in indices:
			[row, column, box] = git(x[0], x[1], posDict)
			
			for d in [row, column, box]:
				for i in d.keys():
					if len(d[i]) == 1:
						puzzle[d[i][0][0]][d[i][0][1]] = i
		
		indices = []
		for i in range(9):
			for j in range(9):
				if puzzle[i][j] == 0:
					indices.append((i, j))
		
		for x in posDict.keys():
			if len(posDict[x]) == 1:
				puzzle[x[0]][x[1]] = posDict[x][0]
	
	"""return the solved puzzle as a 2d array of 9 x 9"""
	return puzzle