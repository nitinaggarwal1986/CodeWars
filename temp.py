def calc(expr):
	print ("\n Current expression is " + expr)
	arr = expr.split()
	
	if len(arr) == 0:
		return 0
	
	arr1 = ""
	
	op = arr.pop()
	
	counter = 0
	result = 0	
		
	if op in ['+', '-', '*', '/']:
		for i in range(len(arr)):
			temp = arr.pop()
			
			if temp not in ['+', '-', '*', '/']:
				arr1 = temp + " " + arr1
				if counter > 0:
					counter -= 1
				print (arr1)
				print (arr)
				print("Counter is %r" % counter)
				if counter == 0:
					print(counter)
					result = eval( str(calc(" ".join(arr))) + " " + op + " " + str(calc(arr1)))
					print(str(calc(" ".join(arr))) + " " + op + " " + str(calc(arr1)))
					print("= %r " % result)
			else:
				arr1 = temp + " " + arr1
				print(arr1)
				if counter >0:
					counter += 1
				else:
					counter += 2
				print("Counter is %r" % counter)
	else:
		print("returning %r" % float(op))
		return float(op)
		
	return result