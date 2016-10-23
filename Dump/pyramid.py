def is_correct_flow(flow):
    n = len(flow)
    for i in range(n):
        if flow[n-i-1] - flow[n-i] not in [-1, 0, 1]:
            return False
    return True

def flow_region(pyramid, flow):
    if not is_correct_flow or len(pyramid) != len(flow):
        return False

    alt = []
    for i in range(len(flow)):
        alt.append(set([flow[i]-1, flow[i]+1, flow[i]]) & set(range(i+1)))
    
	alt = [list(a) for a in alt]
    
    return alt

def alt_flows(alt):
	result = []
	n = len(a)
	if n == 0:
		return None
	def options(temp, current):
		result = []
		if len(temp) == 0:
			return current
		
		for i in range(len(temp[0])):
			for j in range(len(current)):
				result.append(current[j]+[temp[0][i]])
		return options(temp[1:], result)
	
	result = options(alt, [])
	
	result = [x for x in results if is_correct_flow(x)]
	
	return result
	
def improve_flow(pyramid, flow):
    

def longest_slide_down(pyramid):
    # TODO: write some code...
    ind = 0
    sorte = []
    result = pyramid[0][0]
    for i in range(len(pyramid)):
        sorte.append(sorted(range(len(pyramid[i])), key = lambda x: pyramid[i][x]))
    return sorte
