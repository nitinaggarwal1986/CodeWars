def interpret(code):
	
	arr = [[y for y in x] for x in code.split('\n')]
	print(arr)
	output = ""
	stack = ""
	
	from numpy import random
	
	bDict = {
		'0' : lambda output: '0' + output,
		'1' : lambda output: '1' + output,
		'2' : lambda output: '2' + output,
		'3' : lambda output: '3' + output,
		'4' : lambda output: '4' + output,
		'5' : lambda output: '5' + output,
		'6' : lambda output: '6' + output,
		'7' : lambda output: '7' + output,
		'8' : lambda output: '8' + output,
		'9' : lambda output: '9' + output,
		'+' : lambda output: str(int(output[0]) + int(output[1])) + output[2:],
		'-' : lambda output: str(int(output[0]) - int(output[1])) + output[2:],
		'*' : lambda output: str(int(output[0]) * int(output[1])) + output[2:],
		'/' : lambda output: str(int(output[0]) / int(output[1])) + output[2:],
		'%' : lambda output: str(int(output[0]) % int(output[1])) + output[2:],
		'!' : lambda output: '1' + output[1:] if output[0] == '0' else '0',
		"'" : lambda output: '1' + output[2:] if output[0] < output[1] else '0',
		
		'>' : lambda x, y: [x, y + 1], 
		'<' : lambda x, y: [x, y - 1],
		'v' : lambda x, y: [x + 1, y],
		'^' : lambda x, y: [x - 1, y],
		
		'?' : random.choice(['>','<','v','^']),
		
		'_' : lambda output: [output[1:], '>'] if output[1] == 0 else [output[1:], '<'], 
		'|' : lambda output: [output[1:], '^'] if output[1] == 0 else [output[1:], 'v'],
		
		'"' : lambda output, a: [str(ord(a)) + output, 0] if a != '"' else [output, 1],
		
		':' : lambda output: output[0] + output if len(output) > 0 else "0",
		'\\' : lambda output: output[1] + output[0] + output[2:] if len(output) > 1 else output +'0',
		
		'$' : lambda output: output[1:],
		
		'.' : lambda output: [output[1:], stack + str(int(output[0]))],
		',' : lambda output: [output[1:], stack +  chr(int(output[0]))],
		
		'#' : lambda x, y, t: t(x, y),
		
		'p' : lambda p, q, v, arr: ord(v),
		'g' : lambda p, q, output: str(ord(arr[p][q])) + output,
		
		'@' : lambda output, x, y: [output, x, y, 1],
		' ' : lambda output, x, y: [output, x, y, 1]
	}
	
	t = 0
	move = None
	current = arr[0][0]
	x = 0
	y = 0
	
	while( current != '@' ):
		
		if current in ['>', '<', 'v', '^']:
			move = bDict[current]
		elif current == '?':
			move = bDict[bDict['?']]
		elif current in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '%', '!', "'", ":", "\\", '$']:
			output = bDict[current](output)
		elif current in ['_', '|']:
			print(x, y)
			[output, dir] = bDict[current](output)
			move = bDict[dir]
			print(x, y)
		elif current == '"':
			stop = 0
			while (not stop):
				[output, stop] = bDict['"'](output, current)
				x, y = move(x, y)
				current = arr[x][y]
		elif current in ['.', ',']:
			[output, disp] = bDict[current](output)
			stack = stack + str(disp)
		elif current == '#':
			x, y = bDict[current](x, y, move)
		elif current == 'p':
			a = bDict['.'][1]
			b = bDict['.'][1]
			c = bDict[','][1]
			arr[b][a] = c
		elif current == 'g':
			a = bDict['.'][1]
			b = bDict['.'][1]
			output = int(ord(arr[b][a])) + output
		elif current == ' ':
			pass
		else:
			pass
			
		x, y = move(x, y)
		current = arr[x][y]
		print("x = %r, y = %r, current = %r. \n output = %r" % (x, y, current, output))
		
		print("output is actually %r" % stack)	
	return output