from math import factorial

def combination(n, r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))

print(combination(100, 10))