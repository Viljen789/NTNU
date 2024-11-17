def aritmetisk_sum(n, a1, d):
    """
    Beregner summen av en aritmetisk rekke.
    n: antall ledd
    a1: første ledd
    d: differansen mellom leddene
    """
    an = a1 + (n - 1) * d
    sum_rekke = n * (a1 + an) / 2
    return sum_rekke


#Eksempel:
n = 10 
a1 = 1 
d = 2  

print(f"Summen av den aritmetiske rekken er: {aritmetisk_sum(n, a1, d)}")
