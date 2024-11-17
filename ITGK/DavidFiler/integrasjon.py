import numpy as np


def f(x):
    return x**2  # Eksempel: f(x) = x^2


def rektangelmetoden(a, b, n, metode="venstre"):
    """
    Beregner integralet av f(x) fra a til b ved bruk av rektangelmetoden.
    metode: 'venstre', 'høyre' eller 'midt'
    """
    dx = (b - a) / n
    if metode == "venstre":
        x = np.linspace(a, b - dx, n)
    elif metode == "høyre":
        x = np.linspace(a + dx, b, n)
    elif metode == "midt":
        x = np.linspace(a + dx / 2, b - dx / 2, n)
    else:
        raise ValueError("Må ver 'venstre', 'høyre' eller 'midt'")
    integral = np.sum(f(x) * dx)
    return integral


def trapesmetoden(a, b, n):
    """
    Integralet av f(x) frå a til b vha trapesmetoden.
    """
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    integral = (dx / 2) * np.sum(y[:-1] + y[1:])
    return integral


#Eksempel
a = 0  # Nedre grensa
b = 1  # Øvre grensa
n = 100  #Intervall

integral_venstre = rektangelmetoden(a, b, n, metode="venstre")
integral_høyre = rektangelmetoden(a, b, n, metode="høyre")
integral_midt = rektangelmetoden(a, b, n, metode="midt")
integral_trapes = trapesmetoden(a, b, n)

print(f"Rektangelmetoden (venstre): {integral_venstre}")
print(f"Rektangelmetoden (høyre): {integral_høyre}")
print(f"Rektangelmetoden (midtpunkt): {integral_midt}")
print(f"Trapesmetoden: {integral_trapes}")
