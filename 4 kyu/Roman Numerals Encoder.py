def solution(n):
    dict = {1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 
            10 : "X", 40 : "XL", 50 : "L", 90 : "XC", 
            100 : "C", 400: "CD", 500 : "D", 900 : "CM",
            1000 : "M"}
    
    x = [int(x) for x in str(n).zfill(4)]
    result = ""
    if n >= 4000:
        return False
    
    for i in range(4):
        if x[i] > 0 and x[i] < 4:
            result = result + dict[10 ** (4-i-1)] * x[i]
        elif x[i] in [4, 5, 9]:
            result = result + dict[x[i] * 10 ** (4-i-1)]
        elif x[i] > 5 and x[i] < 9:
            result = result + dict[5 * 10 ** (4-i-1)] + dict [10 ** (4-i-1)] * (x[i] - 5)
    return result