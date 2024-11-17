def geometrisk_sum(n, a1, r):
    """
    Beregner summen av en geometrisk rekke.
    n: antall ledd
    a1: første ledd
    r: kvotienten mellom leddene
    """
    if r == 1:
        sum_rekke = n * a1
    else:
        sum_rekke = a1 * (1 - r**n) / (1 - r)
    return sum_rekke


#Eks
n = 5  
a1 = 2  
r = 3  

print(f"Summen av den geometriske rekken er: {geometrisk_sum(n, a1, r)}")
