# m = [x for x in range(1, 100) if any(x%y==0 for y in [z for z in range(2, 10) if all(z%i!=0 for i in range(2, z))]) and not x in [d for d in range(2, 100) if all(d%e!=0 for e in range(2, d))]]
# f = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]
# k = set(m)
# p = set(f)
# print(k^p)

# print(sorted(list(set([x+y for x in range(2, 100) for y in range(2, 100) if all(x%p!=0 for p in range(2, x)) if all(y%p!=0 for p in range(2, y)) if all((x+y)%p!=0 for p in range(2, x+y))]))))
# print(sorted(list(set([x+2 for x in range(2, 100) if all(x%p!=0 for p in range(2, x)) if all((x+2)%p!=0 for p in range(2, x+2))]))))
# # Lag en liste med alle tallene fra 1 til 1000 som ikke kan deles med noen primtall mellom 2 og 10, og som ikke er primtall selv.
# print([x for x in range(1, 1000) if any(x%p==0 for p in range(2, x)) if all(x%p!=0 for p in [q for q in range(2, 10) if all(q%g!=0 for g in range(2, q))])])
# print([x for x in range(10)])

# d = {1:"2", 4:"3", 6:"3"}
# for (key, in d:print(key)

# print([(x,y) for x in range(3) for y in range(5)])

# for i in range(5):
#     for k in range(3):
#         print(i, k)


# print([x for x in range(2, 100) if all(x%p!=0 for p in range(2, x))])

# l = [1, 2, 3, 4, 5, 6, 2, 4, 4]
# f = {}
# for i in l:
#     f[i] = f.get(i, 0)+1
# print(f)
# Example input and output
text = "Viljen"
# Vowels are 'e', 'a', 'a', 'a', reverse them to 'a', 'a', 'a', 'e'
# Expected output: 'axtravaganze'
l = "".join([x if x not in ["a", "e", "i", "o", "u"] else sorted([v for v in text if v in ["a", "e", "i", "o", "u"]])[sum(1 for z in text[:i] if z in ["a", "e", "i", "o", "u"])] for i, x in enumerate(text)])
# alphabet = "abcdefghijklmnopqrstuvwxyz"
print(l)

# # Example input and output
# text = "wizard"
# # Expected output: 'ykzbtf'
# ceasar = [alphabet[(alphabet.index(x)+2)%len(alphabet)] for x in "wizard"]
# # t = [x if x % 2 == 0 else x + 1 for x in range(10)]

# text = "abacabad"
# # Expected output: ['aba', 'aca', 'bacab', 'aba']
# pal = [x for x in [y for y in ]]


# text = "Hello, World!"
# k = 5


# ceasar = [alphabet[(alphabet.index(x)+k)%len(alphabet)] if x.lower() in alphabet else x for x in "wizard"]

# print(l)
# # for a, i in enumerate(text):
# #     print(a, i)


# # print([x for x in range(1, 100) if all()])
# # k = ["b", "d", "c","e", "a", "h"]
# # print(sorted(k)[3])