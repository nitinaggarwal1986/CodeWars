def rot(strng):
    return "".join([strng[len(strng)-i-1] for i in range(len(strng))])

def selfie_and_rot(strng):
    n = strng.count("\n") + 1
    s = strng.replace("\n", "." * n + "\n") + "." * n
    return s + "\n" + rot(s)

def oper(fct, s):
    return fct(s)