def decodeBitsAdvanced(bits):
    
    
    bits = bits.strip('0')
    
    if len(bits) == 0:
        return ""
    elif len(bits) == 1:
        return "."
    
    bits = bits.replace("10", "1 0").replace("01", "0 1")
    
    arr = [len(x) for x in bits.split( ) if x != '']
    arr = [x for x in arr if x != 0]
    
    
    if max(arr) < 2.1 * min(arr):
        tr = .6 * min(arr)
    else:
        temp = sum(arr) / len(arr)
        
        tp = {x: arr.count(x) for x in arr if x != 1}
        temp1 = tp.keys()[tp.values().index(max(tp.values()))]
        
        removed = [x for x in tp.keys() if 4 * tp[x] * tp[x] <  len(arr)]
        
        arr = [x for x in arr if x not in removed]
        
        while (len(set(arr)) > 2 and max(arr) > 5 * temp):
            arr = [x for x in arr if x != max(arr)]
        while(len(set(arr)) > 2 and temp > 2.8 * min(arr)):
            arr = [x for x in arr if x != min(arr)]
        
        tr = min(arr)
    
    arr = [len(x) for x in bits.split( ) if x != '']

    dictS = {x : '.' if float(x) / tr < 2.5 else '-' for x in arr}
    
    result = ""

    for x in bits.split():
        if x[0] == '1':
            result = result + dictS[len(x)]
        elif len(x) > 5.4 * tr:
            result = result + "   "
        elif len(x) < 2.4 * tr:
            result = result + ""
        else:
            result = result + " "
    
    return result

   
def decodeMorse(morseCode):
    
    return " ".join(["".join([MORSE_CODE[char] for char in word.split(" ") if char in MORSE_CODE.keys()]) for word in morseCode.split("   ")])