def brain_luck(code, input):
    arr = [x for x in code]
    output = ""
    memory = chr(0)
    #print(code)
    
    bDict = {
        '>' : lambda y: y + 1, 
        '<' : lambda y: y - 1,
        '+' : lambda y, memory: memory[: y] + chr((ord(memory[y]) + 1) % 256) + memory[y + 1 :] if y < len(memory) else memory[: y] + chr((ord(memory[y]) + 1) % 256),
        '-' : lambda y, memory: memory[: y] + chr((ord(memory[y]) - 1) % 256) + memory[y + 1 :] if y < len(memory) else memory[: y] + chr((ord(memory[y]) - 1) % 256),
        '.' : lambda y, memory, output: output + memory[y],
        ',' : lambda y, input, memory: [memory[: y] + input[0] + memory[y + 1 :] if y < len(memory) else memory[: y] + input[0], input[1:]],
        '[' : lambda y, memory: '>' if memory[y] != chr(0) else ']',
        ']' : lambda y, memory: '>' if memory[y] == chr(0) else '['
    }
    
    t = 0
    y = 0
    stack = []
    
    while (t < len(arr)):
        
        command = arr[t]

        if command in ['>', '<']:
            y = bDict[command](y)
            t += 1
        elif command in ['+', '-']:
            memory = bDict[command](y, memory)
            t += 1
        elif command == '.':
            output = bDict[command](y, memory, output)
            t += 1
        elif command == ',':
            [memory, input] = bDict[command](y, input, memory)
            t += 1
        elif command in ['[',']']:
            #print(command, y, t, memory[y])
            ch = bDict[command](y, memory)
            #print(ch)
            if ch == '>':
                t += 1
            elif ch in [']', '[']:
                ch1 = '[' if ch == ']' else ']'
                r = 1 if ch == ']' else -1
                while(arr[t] != ch or len(stack) != 0):
                    t += r
                    #print(stack, arr[t])
                    if arr[t] == ch1:
                        stack.append(ch1)
                    elif arr[t - r] == ch and len(stack) != 0:
                        if stack[-1] == ch1:
                            stack = stack[:-1]
                        else:
                            stack.append(ch)
        #print(command, memory, input, output, y, t)
        if y == len(memory):
            memory = memory + chr(0)
        
    return output