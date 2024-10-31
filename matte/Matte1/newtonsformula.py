from math import *


def f(x):
    return cosh(x)-x-1

def newtons_formula(x):
    return x - f(x)/f_prime(x)

def f_prime(x):
    return sinh(x)-1

x = 1
for i in range(10):
    x = newtons_formula(x)
    print(x)
