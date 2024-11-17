import numpy as np
from scipy.integrate import quad


def buelengde(f, df, a, b):
   # Beregner lengden funksjonen gitt ved funksjonen f(x) mellom x = a og x = b.
    integrand = lambda x: np.sqrt(1 + (df(x)) ** 2)
    L, _ = quad(integrand, a, b)
    return L

# Eksempel:
def f(x):
    return np.sin(x)


def df(x):
    return np.cos(x)


a = 0
b = np.pi

lengde = buelengde(f, df, a, b)
print(f"Buelengden til funksjonen mellom x = {a} og x = {b} er: {lengde}")
