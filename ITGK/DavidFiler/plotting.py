import numpy as np
import matplotlib.pyplot as plt


def plotte_funksjon(f, a, b, n=1000):
    #Plot frå a->b med n punkt
    x = np.linspace(a, b, n)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Graf av funksjonen f(x)")
    plt.grid(True)
    plt.show()


# Eksempelbruk:
def f(x):
    return np.sin(x) * np.exp(-x / 5)


plotte_funksjon(f, 0, 20)
