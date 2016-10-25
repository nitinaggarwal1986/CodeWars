import re

def tokenize(inp):
    if inp == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(inp)
    return [s for s in tokens if not s.isspace()]
    
class Interpreter:
    
    letters = [chr(x) for x in range(ord('a'), ord('z')+1)] + [chr(x) for x in range(ord('A'), ord('Z')+1)]
    digits = [str(x) for x in range(0, 10)]
    operators = ['+', '-', '*', '/', '%']
    brackets = ['(', ')']
    assign = ['=']
    
    operatorsD = {
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '/' : lambda x, y: x / y,
        '*' : lambda x, y: x * y,
        '%' : lambda x, y: x % y
    }
    
    def __init__(self):
        self.vars = {}
        self.functions = {}
    
    def tonumber(self, x):
        a = 0
        try:
            a = float(x)
        except ValueError:
            return None
        
        if a == int(a):
            return int(a)
        else:
            return a
    
    def input(self, expression):
        tokens = tokenize(expression)
        numbers = []
        print(expression, tokens)
        if len(tokens) == 0:
            return ""
        
        
        for x in tokens:
            try:
                float(x)
                numbers.append(x)
            except ValueError:
                pass
        
        
        for x in tokens:
            if x not in self.operators + self.brackets + self.assign and x not in numbers:
                if x not in self.vars.keys():
                    self.vars[x] = None
        
        print(sum([int(x in self.operators or x == '=') for x in tokens]))
        
        if len(tokens) >= 2 and sum([int(x in self.operators or x == '=') for x in tokens]) == 0:
            raise RuntimeError("Not a valid expression")
            return "Error: Not a valid expression"
        elif len(tokens) == 1 and tokens[0] not in numbers:
            if tokens[0] in self.vars.keys() and self.vars[tokens[0]] != None:
                tp = float(self.vars[tokens[0]])
                return int(tp) if tp == int(tp) else tp
            else:
                raise RuntimeError("Invalid identifier. No variable with name '" + tokens[0] + "' was found.")
                return "ERROR: Invalid identifier. No variable with name '" + tokens[0] + "' was found."
        
        if len(tokens) == 1 and tokens[0] in numbers:
            return self.tonumber(tokens[0])
        elif len(tokens) == 2 and tokens[0] == "-" and tokens[1] in numbers:
            return str(-1 * float(tokens[1]))
        elif len(tokens) == 3 and tokens[1] in self.operatorsD.keys() and tokens[0] in numbers and tokens[2] in numbers:
            return self.tonumber(str(self.operatorsD[tokens[1]](float(tokens[0]), float(tokens[2]))))
        elif len(tokens) == 4 and tokens[1] in self.operatorsD.keys() and tokens[0] in numbers and tokens[3] in numbers and tokens[2] == "-":
            return self.tonumber(self.tonumber(str(self.operatorsD[tokens[1]](float(tokens[0]), -1 * float(tokens[3])))))
        elif len(tokens) == 4 and tokens[2] in self.operatorsD.keys() and tokens[1] in numbers and tokens[3] in numbers and tokens[0] == "-":
            return self.tonumber(str(self.operatorsD[tokens[2]](-1 * float(tokens[1]), float(tokens[3]))))
        elif len(tokens) == 5 and tokens[2] in self.operatorsD.keys() and tokens[1] in numbers and tokens[4] in numbers and tokens[0] == "-" and tokens[3] == "-":
            return self.tonumber(str(self.operatorsD[tokens[2]](-1 * float(tokens[1]), -1 * float(tokens[4]))))
        
        
        
        
        if len(tokens) > 2 and tokens[1] == '=':
            if tokens[0] in self.vars.keys():
                self.vars[tokens[0]] = str(self.input("".join(tokens[2:])))
                return self.tonumber(self.vars[tokens[0]])
        
        varLoc = [x in self.vars.keys() for x in tokens]
        opLoc = [x in self.operators for x in tokens]
        
        stack = {x : [] for x in self.brackets}
        
        for i in range(len(tokens)):
            if tokens[i] in self.vars.keys():
                if self.vars[tokens[i]] != None:
                    tokens[i] = self.vars[tokens[i]]
                else:
                    raise RuntimeError(tokens[i] + " is an undefined variable.")
                    return tokens[i] + " is an undefined variable."
            if tokens[i] in self.brackets:
                stack[tokens[i]].append(i)
        
        lc = len(stack['('])
        rc = len(stack[')'])
        
        if lc != rc:
            return "Wrong Brackets"
        
        a = stack['(']
        b = stack[')']
        
        bktD = {} 
        
        while(len(a) != 0):
            
            mx = max(a)
            mn = min([y for y in b if y > mx])
            
            a = [x for x in a if x != mx]
            b = [x for x in b if x != mn]
            
            bktD[mx] = mn
        
            
        bkts = list(bktD.keys()) + list(bktD.values())

        min1 = -1
        
        tokensC = []
        for i in sorted(list(bktD.keys())):
            if i >= min1:
                tokensC = tokensC + tokens[min1 + 1 : i] + [str(self.input("".join(tokens[i + 1: bktD[i]])))]
                min1 = bktD[i] 
                print(tokensC)
        
        tokensC = tokensC + tokens[min1 + 1: ]
        
        levels = {}
        
        tokensD = []
        min2 = -1
        print("Check: ", tokensC)
        for i in range(len(tokensC)):
            
            if i > min2 and i + 2 < len(tokensC) and tokensC[i + 1] in ['*', '/', '%']:
                tokensD = tokensD + tokensC[min2 + 1 : i] + [self.operatorsD[tokensC[i + 1]](float(tokensC[i]), float(tokensC[i+2]))]
                min2 = i + 2
        tokensD = tokensD + tokensC[min2 + 1: ]
        tokensE = []
        min3 = -1
        print("Check2: ", tokensD)
        for i in range(len(tokensD)):
            
            if i > min3 and i + 2 < len(tokensD) and tokensD[i + 1] in ['+', '-']:
                tokensE = tokensE + tokensD[min3 + 1 : i] + [self.operatorsD[tokensD[i + 1]](float(tokensD[i]), float(tokensD[i+2]))]
                min3 = i + 2
        tokensE = tokensE + tokensD[min3 + 1: ]
        tokensE = [str(x) for x in tokensE]
        print(tokensE)
        return self.tonumber(str(self.input("".join(tokensE))))