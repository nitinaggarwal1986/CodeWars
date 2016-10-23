def nbr_of_laps(x, y):
    m = x * y
    a = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            a.append(i)
    
    m = m / max(a)
    
    return [m / x, m / y]