def permutations(string):
	
	if len(string) == 1:
		return [string]
	
	def pop(strin, i):
		starr = []
	
		for l in range(len(strin)):
			if l != i:
				starr.append(strin[l])
		return "".join(starr)
	
	perms = []
	
	for i in range(len(string)):
		for x in permutations(pop(string, i)):
			if x not in perms:
				perms.append(string[i] + x)
	filter = []
	
	for x in perms:
		if x not in filter:
			filter.append(x)
	return filter