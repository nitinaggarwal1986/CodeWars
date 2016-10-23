def code(s):
    l = len(s)
    n = 0
    while (n ** 2 < l):
        n += 1
    s = s + chr(11) * (n ** 2 - l)
    t = []
    for i in range(n):
        t.append(s[i*n + 0: i*n + n])
    result = [""] * n
    for row in t:
        for i in range(n):
            result[i] = row[i] + result[i]
    return "\n".join(result)
        

def decode(s):
    t = s.split("\n")
    n = len(t[0])
    result = [""] * n
    for row in t:
        for i in range(n):
            result[i] = result[i] + row[n - i - 1]
    return "".join(result).strip(chr(11))