import matplotlib.pyplot as plt


def plotte_følge(følge_formel, n_terms):
    """
    Plotter de første n_terms leddene i en følge.
    """
    n_values = range(1, n_terms + 1)
    a_n = [følge_formel(n) for n in n_values]
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, a_n, "o-", label="a_n")
    plt.xlabel("n")
    plt.ylabel("a_n")
    plt.title("Visualisering av følge")
    plt.grid(True)
    plt.legend()
    plt.show()


# Eksempelbruk:
def følge_formel(n):
    return 1 / n


n_terms = 50
plotte_følge(følge_formel, n_terms)
