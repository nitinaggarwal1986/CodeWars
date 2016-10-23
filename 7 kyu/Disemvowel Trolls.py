def disemvowel(string):
    return ''.join([x for x in string if x not in ['a','A','e','E','i','I','o','O','u','U']])