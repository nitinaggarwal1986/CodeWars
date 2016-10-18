class Morse:
	@classmethod
	def encode(self,message):
		result = ""
		space = 1
		for x in message:
			if x == ' ':
				result = result + "0000000"
				space = 1
			else:
				if space:
					result = result + Morse.alpha[x]
					space = 0
				else:
					result = result + "000" + Morse.alpha[x]
		result = result + "0" * (32 - len(result) % 32)
		
		listR = []
		for i in range(int(len(result) / 32)):
			temp = int(result[32 * i + 0 : 32 * i + 32], 2) - (1 << 32)
			check = 2 ** 31
			num = temp if temp >= (0 - check) else check * 2 + temp
			listR.append(num)
		
		return listR
		
	@classmethod
	def decode(self,array):
		string = ""
		check = 2**32
		for x in array:
			if x < 0:
				string = string + bin(check + x)[2:].zfill(32)
			else:
				string = string + bin(x)[2:].zfill(32)
		while string[len(string) - 1] == '0':
			string = string[:len(string) - 1]
		
		words = []
		for x in [a.split('000') for a in string.split('0000000')]:
			temp = ""
			for i in x:
				try:
					if i != "":
						temp = temp + list(Morse.alpha.keys())[list(Morse.alpha.values()).index(i)]
				except ValueError:
					pass
			words.append(temp)
		
		return " ".join(words).strip()
		
	alpha = {
		'A': '10111',
		'B': '111010101',
		'C': '11101011101',
		'D': '1110101',
		'E': '1',
		'F': '101011101',
		'G': '111011101',
		'H': '1010101',
		'I': '101',
		'J': '1011101110111',
		'K': '111010111',
		'L': '101110101',
		'M': '1110111',
		'N': '11101',
		'O': '11101110111',
		'P': '10111011101',
		'Q': '1110111010111',
		'R': '1011101',
		'S': '10101',
		'T': '111',
		'U': '1010111',
		'V': '101010111',
		'W': '101110111',
		'X': '11101010111',
		'Y': '1110101110111',
		'Z': '11101110101',
		'0': '1110111011101110111',
		'1': '10111011101110111',
		'2': '101011101110111',
		'3': '1010101110111',
		'4': '10101010111',
		'5': '101010101',
		'6': '11101010101',
		'7': '1110111010101',
		'8': '111011101110101',
		'9': '11101110111011101',
		'.': '10111010111010111',
		',': '1110111010101110111',
		'?': '101011101110101',
		"'": '1011101110111011101',
		'!': '1110101110101110111',
		'/': '1110101011101',
		'(': '111010111011101',
		')': '1110101110111010111',
		'&': '10111010101',
		':': '11101110111010101',
		';': '11101011101011101',
		'=': '1110101010111',
		'+': '1011101011101',
		'-': '111010101010111',
		'_': '10101110111010111',
		'"': '101110101011101',
		'$': '10101011101010111',
		'@': '10111011101011101',
		' ': '0'
		}
