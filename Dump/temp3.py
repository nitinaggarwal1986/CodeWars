def permutations(string):
	
	def switch(strin, i, j):
		starr = []
	
		for l in range(len(strin)):
			starr.append(strin[l])
		x = starr[i]
		starr[i] = starr[j]
		starr[j] = x
		
		return "".join(starr)
		
		
	perms = [string]
	k = 0
	for st in perms:
		k = len(perms)
		for j in range(1, len(string)):
			temp = switch(st, 0, j)
			if temp not in perms:
				perms.append(temp)
		if k == len(perms):
			break
	return perms

print(permutations("aabb"))