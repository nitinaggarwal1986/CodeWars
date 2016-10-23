def sum_for_list(lst):
    
    def isPrime(num):
        from math import sqrt
        max = int(sqrt(abs(num)))
        
        for x in range(2, max + 2):
            if num % x == 0 and num > x:
                return False
                
        return True
    
    maxNum = max([abs(x) for x in lst])
    result = []
    
    for i in [x for x in range(2, maxNum) if isPrime(x)]:
        temp = []
        check = 0
        for x in lst:
            if x % i == 0:
                temp.append(x)
                check += 1
        if check:
            result.append([i, sum(temp)])
    return result