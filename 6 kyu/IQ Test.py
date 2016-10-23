def iq_test(numbers):
    temp = [int(x)%2 for x in numbers.split()]
    ind = {i: temp.count(i) for i in [0,1]}
    
    return temp.index(ind.values().index(1)) + 1