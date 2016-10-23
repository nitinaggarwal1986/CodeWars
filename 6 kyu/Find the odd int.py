def find_it(seq):
    temp = {}
    for x in seq:
        temp[x] = seq.count(x)
        if temp[x] % 2:
            return(x)