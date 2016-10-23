def zeros(n):
    
    x = n
    zeroes = 0
    while (x > 0):
        zeroes += int(x / 5)
        x = int(x / 5)
    return (zeroes)