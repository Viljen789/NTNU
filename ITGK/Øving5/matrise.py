import random
def random_matrise(h, b):
    return [[random.randrange(10)*1 for i in range(h)]for x in range(b)]

def print_matrise(l, n):
    return n + "=[\n[" + "]\n[".join([",".join(map(str, sub)) for sub in l]), "]\n]"
def matrise_addisjon(a, b):
    return ["Matrisene er ikke av samme dimensjon"] if (len(a)!=len(b) or len(a[0])!=len(b[0])) else [[a[j][i]+b[j][i]for i in range(len(a[0]))]for j in range(len(a))]


# print(*print_matrise(random_matrise(3, 5), "A"))
# A = random_matrise(3, 5)
# B = random_matrise(3, 5)
# print(*print_matrise(A, "A"))
# print(*print_matrise(B, "A"))
# print(*print_matrise(matrise_addisjon(A, B), "A+B"))
print(*print_matrise(matrise_addisjon(random_matrise(3, 5), random_matrise(3, 5)), "A+B"))
