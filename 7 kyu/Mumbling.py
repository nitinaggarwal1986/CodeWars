def accum(s):
    e = [x.upper() for x in s]
    return "-".join(["".join([e[i]] + [e[i].lower() for x in range(i)]) for i in range(len(e))])