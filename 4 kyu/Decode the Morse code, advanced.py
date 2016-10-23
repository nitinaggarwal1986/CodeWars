def decodeBits(bits):
    print(bits)
    def removeTail(bits):
        while(bits[-1] == '0'):
            bits = bits[:-1]
        while(bits[0] == '0'):
            bits = bits[1:]
        return bits
    
    bits = removeTail(bits)
    def oneTail(bits):
        n = 0
        while(bits[-1-n] == '1'):
            n = n + 1
            if n > len(bits) - 1:
                break
        return n
    
    n = oneTail(bits)
    
    """
    This n is at least a multiple of the transmission rate.
    """
    options = []

    for i in range(1, n + 1):
        if n % i == 0:
            options.append(i)
    
    """
    The transmission rate should also divide the sum of all the
    ones present in the bit
    """
    
    m = sum([int(i) for i in bits])
    
    options = [x for x in options if m % x == 0]
    rejected = []
    counter = 0
    
    for x in options:
        counter = 0
        for i in bits:
            if i == '1':
                counter += 1
            else:
                if counter % x != 0:
                    rejected.append(x)
                counter = 0     
    
    for x in options:
        counter = 0
        for i in bits:
            if i == '0':
                counter += 1
            else:
                if counter % x != 0:
                    rejected.append(x)
                counter = 0 
    
    
    options = [x for x in options if x not in rejected]

    pr = max(options)
    print(pr)
    reduced = ""
    
    for i in range(len(bits)):
        if i % pr == 0:
            reduced = reduced + bits[i]
            
    return reduced.replace('111', '-').replace('000000', '   ').replace('1', '.').replace('000', ' ').replace('0', '')
    
def decodeMorse(morseCode):
    
    return " ".join(["".join([MORSE_CODE[char] for char in word.split(" ") if char in MORSE_CODE.keys()]) for word in morseCode.split("   ")])