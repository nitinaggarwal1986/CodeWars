def toAscii85(data):
	
	if data == '':
		return '<~~>'
	
	arr = [format(ord(ch), 'b').zfill(8) for ch in data]
	
	bits32 = ["".join(arr[4 * i: 4 * i + 4]) for i in range(int(len(arr) / 4))]
	
	tail = 0
	
	if len(arr) % 4 != 0:
		bits32.append("".join(arr[4 * int(len(arr) / 4) : ]) + "0" * (32 - len(arr) % 4 * 8 ))
		tail = int((32 - len(arr) % 4 * 8 ) / 8)
	ints = [int(b, 2) for b in bits32]
	
	def to85(num):
		
		result = []
		dump = num
		result.append(int(dump / 85 ** 4))
		
		for i in range(1, 5):
			dump = dump - result[len(result) - 1] * 85 ** (5 - i)
			result.append(int(dump / 85 ** (4 - i)))
	
		return [x + 33 for x in result]
	
	base85 = [to85(x) for x in ints]
	
	chars = "<~" + "".join(["".join([chr(y) for y in x]) for x in base85 ]) + "~>"
	
	if tail != 0:
		chars = chars[:len(chars)- tail - 2]
		chars = chars + "~>"
	
	tp = []
	charf = '<~'
	
	for i in range(int(len(chars) / 5)):
		if chars[5 * i + 2 : 5 * i + 7] == "!!!!!":
			tp.append(i)
	
	t = 0
	
	for i in range(int(len(chars) / 5)):
		if i in tp:
			charf = charf + "z"
		else:
			charf = charf + chars[5 * i + 2 : 5 * i + 7]
		t = i
	charf = charf + chars[5 * i + 7:]
	
	return charf

def fromAscii85(data):
	
	data = data.replace(' ', '').replace('\n', '').replace('\t','')
	code = data[2: len(data) - 2].replace('z', '!!!!!')
	
	t = 5 - len(code) % 5
	
	if len(code) % 5 != 0:
		code = code + "u" * (5 - len(code) % 5)
		
	base85 = [[ord(y) for y in code[5 * i : 5 *i + 5]] for i in range(int(len(code) / 5))]
	
	def toint(arr):
		k = len(arr)
		while ( len(arr)!= 5):
			arr.append(33)
		return sum([(arr[i] - 33) * (85 ** (4 - i)) for i in range(5)])
	
	ints = [toint(x) for x in base85]
	bits32 = [format(y, 'b').zfill(32) for y in ints]
	arr = [[x[8 * i : 8 * i + 8] for i in range(4)] for x in bits32]
	
	arr1 = []
	
	for i in range(len(arr)):
		arr1 = arr1 + arr[i]
	return "".join([chr(int(x, 2)) for x in arr1 if int(x, 2) in range(256)])[: len(arr1) - t % 5]
