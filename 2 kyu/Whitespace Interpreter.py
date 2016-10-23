def whitespace(code, inp = ''):

    output = ''
    stack = []
    heap = {}
    location = {}


    if code == "":
        raise RuntimeError("Unclean Termination")

    dictU = {" " : 's', '\t' : 't', '\n' : 'n'}
    code = "".join([x for x in code if x in dictU.keys()])
    code = code.replace(" ", dictU[" "]).replace("\t", dictU["\t"]).replace("\n", dictU["\n"])
    codeR = "".join([x for x in code])
    L = len(codeR)
    print(code)

    def impG(code):
        if code[0] == 's':
            return ["Stack Manipulation", code[1:]]
        elif code[0] == 't':
            if code[1] == 's':
                return ["Arithmetic", code[2:]]
            elif code[1] == 't':
                return ["Heap Access", code[2:]]
            elif code[1] == 'n':
                return ["Input/Output", code[2:]]
        elif code[0] == 'n':
            return ["Flow Control", code[1:]]

    impO = ["Stack Manipulation", "Arithmetic", "Heap Access", "Input/Output", "Flow Control"]



    def numbers(code):
        current = code[0]
        code = code[1:]
        numstr = "" 
        if current == 't':
            numstr = numstr + "-"
        elif current == 's':
            numstr = numstr + "+"
        else:
            raise RuntimeError("Unclean termination of number, sign not decided", codeR)
        
        current = code[0]
        code = code[1:]
        
        if current == 'n':
            return [0, code]
        
        while current != 'n':
            
            if current == 's':
                numstr = numstr + '0'
            elif current == 't':
                numstr = numstr + '1'
            else:
                raise RuntimeError("Unclean termination of number")
            
            if len(code) == 0:
                raise EOFError("Unclean termination of the file.")
            
            current = code[0]
            code = code[1:]
        return [int(numstr, 2), code]

    def labels(code):
        current = code[0]
        code = code[1:]
        lab = ""
        
        while current != 'n':
            lab = lab + current
            
            if len(code) == 0:
                raise EOFError("Unclean termination of the file.")
            
            current = code[0]
            code = code[1:]
        
        
        return [lab, code]

    def input(inp, ch = 0):
        
        inp = inp.translate( { c:"\n" for c in ' \n\t\r' } )
        current = inp[0]
        inp = inp[1:]
        value = ""
        if ch == 0:
            return [current, inp]
        
        while current != '\n':
            value = value + current
            current = inp[0]
            inp = inp[1:]
            
            if len(code) == 0:
                raise EOFError("Unclean termination of the file.")
        
        return [int(value), inp]
        
    def SM(code, stack, comp = 0):
        
        current = code[0]
        code = code[1:]
        
        if current == 's':
            [number, code] = numbers(code)
            stack = [number] + stack
            return [code, stack]
        elif current == 't':
            current = code[0]
            code = code[1:]
            if current == 's':
                [number, code] = numbers(code)
                print(number)
                if 0 <= number <= len(stack):
                    stack = [stack[number]] + stack
                else:
                    raise RuntimeError("Out of bound index")
                return [code, stack]
            elif current == 'n':
                [number, code] = numbers(code)
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack]
                    else:
                        raise RuntimeError("Empty stack")
                
                if number >= 0:
                    stack = [stack[0]] + stack[number + 1:]
                else:
                    stack = [stack[0]]
                return [code, stack]
            else:
                raise RuntimeError("Unclean Stack Management")
        elif current == 'n':
            current = code[0]
            code = code[1:]
            if current == 's':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack]
                    else:
                        raise RuntimeError("Empty stack")
                stack = [stack[0]] + stack
                return [code, stack]
            elif current == 't':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack]
                    else:
                        raise RuntimeError("Empty stack")
                stack = [stack[1], stack[0]] + stack[2:]
                return [code, stack]
            elif current == 'n':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack]
                    else:
                        raise RuntimeError("Empty stack")
                stack = stack[1:]
                return [code, stack]

    def Arth(code, stack):
        
        current = code[0]
        code = code[1:]
        
        if current == 's':
            current = code[0]
            code = code[1:]
            if current == 's':
                stack = [stack[1] + stack[0]] + stack[2:]
                return [code, stack]
            elif current == 't':
                stack = [stack[1] - stack[0]] + stack[2:]
                return [code, stack]
            elif current == 'n':
                stack = [stack[1] * stack[0]] + stack[2:]
                return [code, stack]
        if current == 't':
            current = code[0]
            code = code[1:]
            if current == 's':
                stack = [int(stack[1] / stack[0]) if int(stack[1] / stack[0]) >= 0 else int(stack[1] / stack[0]) -1] + stack[2:] 
                return [code, stack]
            elif current == 't':
                stack = [stack[1] % stack[0]] + stack[2:]
                return [code, stack]
            else:
                raise ArithmeticError("Unclean Arithmetic")
        else:
            raise ArithmeticError("Unclean Arithmetic")
            
    def HA(code, heap, stack):
        
        current = code[0]
        code = code[1:]
        
        if current == 's':
            a = stack[0]
            b = stack[1]
            stack = stack[2:]
            
            heap[b] = a
            return [code, heap, stack]
        elif current == 't':
            a = stack[0]
            stack = [heap[a]] + stack[1:]
            return [code, heap, stack]
        else:
            raise RuntimeError("Unclean Heap Access")

    def IO(code, output, inp, stack, heap, comp = 0):
        
        current = code[0]
        code = code[1:]
        
        if current == 's':
            current = code[0]
            code = code[1:]
            if current == 's':
                if len(stack) == 0:
                    raise RuntimeError("Stack is empty")
                output = output + chr(stack[0])
                stack = stack[1:] if len(stack) > 1 else []
                return [code, output, inp, stack, heap]
            elif current == 't':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, output, inp, stack, heap]
                    else:
                        raise RuntimeError("Empty stack")
                output = output + str(stack[0])
                stack = stack[1:] if len(stack) > 1 else []
                return [code, output, inp, stack, heap]
            else:
                raise IOError("Unclean Input/Output operation")
        elif current == 't':
            current = code[0]
            code = code[1:]
            if current == 's':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, output, inp, stack, heap]
                    else:
                        raise RuntimeError("Empty stack")
                if len(inp) == 0:
                    raise RuntimeError("No input to fetch")

                [a, inp] = input(inp, 0)
                b = stack[0]
                stack = stack[1:] if len(stack) > 1 else []
                heap[b] = ord(a)
                return [code, output, inp, stack, heap]
            elif current == 't':
                if len(stack) == 0:
                    raise RuntimeError("Stack is empty")
                if len(inp) == 0:
                    raise RuntimeError("No input to fetch")

                [a, inp] = input(inp, 1)
                b = stack[0]
                stack = stack[1:] if len(stack) > 1 else []
                heap[b] = int(a)
                return [code, output, inp, stack, heap]
            else:
                raise IOError("Unclean Input/Output operation")
        else:
            raise IOError("Unclean Input/Output operation")

    def FC(code, stack, location, codeR, locS, comp = 0):
        
        current = code[0]
        code = code[1:]
        
        if current == 's':
            current = code[0]
            code = code[1:]
            if current == 's':
            
                [lab, code] = labels(code)
                loc = int(L) - len(code)
                if comp == 1:
                    if lab in location.keys():
                        if location[lab] != loc:
                            raise RuntimeError("Repeated Label", lab)
                    else:
                        location[lab] = loc
                else:
                    location[lab] = loc
                if len(code) == 0:
                    raise RuntimeError("Unclean Termination")
                return [code, stack, L-len(code), location]
            elif current == 't':
                [lab, code] = labels(code)
                locI = L - len(code)
                if lab in location.keys():
                    loc = location[lab]
                    code = "".join([codeR[i] for i in range(L) if i >= loc])
                    return [code, stack, locI, location]
                else:
                    if comp == 1:
                        return  [code, stack, locI, location]
                    else:
                        raise RuntimeError("Unknown Label", lab)
            elif current == 'n':
                [lab, code] = labels(code)
                locI = L - len(code)
                print(lab, location, code)
                if comp == 1:
                    return [code, stack, locI, location]
                    
                if lab in location.keys():
                    loc = location[lab]
                    code = "".join([codeR[i] for i in range(L) if i >= loc])
                    return [code, stack, locI, location]
                else:
                    if comp == 1:
                        return  [code, stack, locI, location]
                    else:
                        raise RuntimeError("Unknown Label", lab)
        elif current == 't':
            current = code[0]
            code = code[1:]
            if current == 's':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack, len(code), location]
                    else:
                        raise RuntimeError("Stack empty")
                a = stack[0]
                stack = stack[1:]
                [lab, code] = labels(code)
                locI = L - len(code)
                print([lab], a, L, code)
                if a == 0:
                    if comp == 1:
                        return [code, stack, locI, location]
                    if lab in location.keys():
                        loc = location[lab]
                        print(loc)
                        code = "".join([codeR[i] for i in range(L) if i >= loc])
                        print(code)
                        return [code, stack, locI, location]
                    else:
                        if comp == 1:
                            return  [code, stack, locI, location]
                        else:
                            raise RuntimeError("Unknown Label")
                else:
                    return [code, stack,locI, location]
            elif current == 't':
                if len(stack) == 0:
                    if comp == 1:
                        return [code, stack, len(code), location]
                    else:
                        raise RuntimeError("Stack empty")
                a = stack[0]
                stack = stack[1:]
                [lab, code] = labels(code)
                locI = L - len(code)
                print(lab, a, stack, code, )
                if a < 0:
                    if comp == 1:
                        return [code, stack, locI, location]
                    if lab in location.keys():
                        loc = location[lab]
                        code = "".join([codeR[i] for i in range(L) if i >= loc])
                        return [code, stack, locI, location]
                    else:
                        if comp == 1:
                            return  [code, stack, locI, location]
                        else:
                            raise RuntimeError("Unknown Label")
                else:
                    return [code, stack, locI, location]
            elif current == 'n':
                locI = L - len(code)
                
                if comp == 1:
                        return [code, stack, locI, location]
                code = "".join([codeR[i] for i in range(L) if i >= locS])
                if locI == locS:
                    raise RuntimeError("Return inside the subroutine call")
                return [code, stack, locI, location]
        elif current == 'n':
            current = code[0]
            code = code[1:]
            if current == 'n':
                if comp == 1:
                    return [code, stack, len(code), location]
                else:
                    return ["", stack, L, location]
            else:
                raise RuntimeError("Unclean Termination")
    locC = 0

    def compiler(code, stack, location, codeR, inp, output, heap, locC):
        while (len(code) != 0):
            
            if len(code) == 1:
                raise RuntimeError("Unclean Termination")
            elif len(code) == 2 and code[1] != 't':
                raise RuntimeError("Unclean Termination")
            imp, code = impG(code)
                    
            if imp == "Flow Control":
                [code, stack, locC, location] = FC(code, stack, location, codeR, locC, 1)
            elif imp == "Arithmetic":
                [code, stack] =  Arth(code, stack)
            elif imp == "Heap Access":
                [code, heap, stack] = HA(code, heap, stack)
            elif imp == "Input/Output":
                [code, output, inp, stack, heap] = IO(code, output, inp, stack, heap, 1)
            elif imp == "Stack Manipulation":
                [code, stack] = SM(code, stack, 1)
            if code == None:
                print("None code")
            elif output == None:
                print("None output")
            elif stack == None:
                print("None stack")
            elif location == None:
                print("None location")
            elif inp == None:
                print("None inp")
            
            print(code, stack, output, location, [x for x in inp])
        return location

    location = compiler("".join([x for x in code]), [], {}, "".join([x for x in codeR]), "".join([x for x in inp]), "", {}, 0)
    print(location)
    
    
    
    while (len(code) != 0):
        
        if len(code) == 1:
            raise RuntimeError("Unclean Termination")
        elif len(code) == 2 and code[1] != 't':
            raise RuntimeError("Unclean Termination")
        
        k = len(code)
        
        imp, code = impG(code)
        
        if imp == "Flow Control":
            [code, stack, locC, location] = FC(code, stack, location, codeR, locC)
        elif imp == "Arithmetic":
            [code, stack] =  Arth(code, stack)
            if len(code) == 0:
                raise RuntimeError("Unclean Termination")
        elif imp == "Heap Access":
            [code, heap, stack] = HA(code, heap, stack)
            if len(code) == 0:
                raise RuntimeError("Unclean Termination")
        elif imp == "Input/Output":
            [code, output, inp, stack, heap] = IO(code, output, inp, stack, heap)
            if len(code) == 0:
                raise RuntimeError("Unclean Termination")
        elif imp == "Stack Manipulation":
            [code, stack] = SM(code, stack)
            if len(code) == 0:
                raise RuntimeError("Unclean Termination")
        
        print(code, stack, location)
        print([x for x in output])
    
    return output