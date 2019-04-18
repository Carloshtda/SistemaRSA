import math

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    top_divisor = math.floor(math.sqrt(num))
    for i in range(3, top_divisor+1, 2):
        if num % i == 0:
            return False
    return True

def aeext(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0
def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = aeext(a, b)
    if g == 1:
        return x % b
