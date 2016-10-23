def is_valid_IP(strng):
    try:
        return sum([ 0<= int(x) < 256 for x in strng.split('.') if x == str(int(x))]) == 4
    except:
        return False