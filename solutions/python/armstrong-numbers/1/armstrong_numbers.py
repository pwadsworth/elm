from functools import reduce

def is_armstrong_number(n:int):
    digits = list(map(int, str(n)))
    exponent = len(digits)
    return n == reduce(lambda acc, x: acc + pow(x, exponent), digits, 0)
