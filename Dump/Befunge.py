def interpret(code):
    
    arr = [[y for y in x] for x in code.split('\n')]
    print(arr, code)
    stack = []
    output = ""
    
    from numpy import random
    
    bDict = {
        '0' : lambda stack: [0] + stack,
        '1' : lambda stack: [1] + stack,
        '2' : lambda stack: [2] + stack,
        '3' : lambda stack: [3] + stack,
        '4' : lambda stack: [4] + stack,
        '5' : lambda stack: [5] + stack,
        '6' : lambda stack: [6] + stack,
        '7' : lambda stack: [7] + stack,
        '8' : lambda stack: [8] + stack,
        '9' : lambda stack: [9] + stack,
        '+' : lambda stack: [int(stack[1]) + int(stack[0])] + stack[2:],
        '-' : lambda stack: [int(stack[1]) - int(stack[0])] + stack[2:],
        '*' : lambda stack: [int(stack[1]) * int(stack[0])] + stack[2:],
        '/' : lambda stack: [int(stack[1]) / int(stack[0])] + stack[2:],
        '%' : lambda stack: [int(stack[1]) % int(stack[0])] + stack[2:],
        '!' : lambda stack: [1] + stack[1:] if stack[0] == 0 else [0] + stack[1:],
        "'" : lambda stack: [1] + stack[2:] if stack[0] < stack[1] else [0] + stack[2:],
        
        '>' : lambda x, y: [x, y + 1], 
        '<' : lambda x, y: [x, y - 1],
        'v' : lambda x, y: [x + 1, y],
        '^' : lambda x, y: [x - 1, y],
        
        '?' : random.choice(['>','<','v','^']),
        
        '_' : lambda stack: [stack[1:], '>'] if stack[0] == 0 else [stack[1:], '<'], 
        '|' : lambda stack: [stack[1:], '^'] if stack[0] == 0 else [stack[1:], 'v'],
        
        '"' : lambda stack, a: [[ord(a)] + stack, 0] if a != '"' else [stack, 1],
        
        ':' : lambda stack: [stack[0]] + stack if len(stack) > 0 else [0],
        '\\' : lambda stack: [stack[1]] + [stack[0]] + stack[2:] if len(stack) > 1 else stack + [0],
        
        '$' : lambda stack: stack[1:],
        
        '.' : lambda stack: [stack[1:], int(stack[0])],
        ',' : lambda stack: [stack[1:], chr(stack[0])],
        
        '#' : lambda x, y, t: t(x, y),
        
        'p' : lambda p, q, v, arr: ord(v),
        'g' : lambda p, q, stack: [ord(arr[p][q])] + stack,
        
        '@' : lambda stack, x, y: [stack, x, y, 1],
        ' ' : lambda stack, x, y: [stack, x, y, 1]
    }
    
    t = 0
    move = bDict['>']
    current = arr[0][0]
    x = 0
    y = 0
    
    while( current != '@' ):
        
        if current in ['>', '<', 'v', '^']:
            move = bDict[current]
        elif current == '?':
            move = bDict[bDict['?']]
        elif current in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '%', '!', "'", ":", "\\", '$']:
            stack = bDict[current](stack)
        elif current in ['_', '|']:
            [stack, dir] = bDict[current](stack)
            move = bDict[dir]
            
        elif current == '"':
            stop = 0
            while (not stop):
                x, y = move(x, y)
                current = arr[x][y]
                [stack, stop] = bDict['"'](stack, current)
                #print(stack)
        elif current in ['.', ',']:
            [stack, disp] = bDict[current](stack)
            output = output + str(disp)
        elif current == '#':
            x, y = bDict[current](x, y, move)
        elif current == 'p':
            a = bDict['.'](stack)[1]
            b = bDict['.'](stack)[1]
            c = bDict[','](stack)[1]
            arr[b][a] = c
        elif current == 'g':
            a = bDict['.'](stack)[1]
            b = bDict['.'](stack)[1]
            stack = int(ord(arr[b][a])) + stack
        elif current == ' ':
            pass
        else:
            pass
            
        x, y = move(x, y)
        current = arr[x][y]
        t += 1
        if t == 300: 
            break
        print("x = %r, y = %r, current = %r. \n stack = %r" % (x, y, current, stack))
        
        print("Output is actually %r" % output)    
        
    return output

interpret('>987v>.v\nv456<  :\n>321 ^ _@')
interpret("08>:1-:v v *_$.@ \n  ^    _$>\:^'")