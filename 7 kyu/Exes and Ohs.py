def xo(s):
    num_x = 0
    num_o = 0
    
    for i in s:
        if i == 'x' or i == 'X':
            num_x += 1
        elif i == 'o' or i == 'O':
            num_o += 1
    return num_x == num_o