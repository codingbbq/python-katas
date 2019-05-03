"""
    Given an integral number, determine if it's a square number:
"""
import math

def is_square(n):
    if(n < 0):
        return False

    sr = math.sqrt(n)
    return sr.is_integer()

print(is_square(2500)) # True
print(is_square(-1)) #False