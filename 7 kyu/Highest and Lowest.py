def high_and_low(numbers):
    return " ".join([str(a([int(x) for x in numbers.split(" ")])) for a in [max, min]])