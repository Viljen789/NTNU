# import pickle 


# l = [x for x in range(2, 100) if all(x%p!=0 for p in range(2, x))]

# with open("prim.pickle", "wb") as f:
#     pickle.dump(l,f)

# with open("prim.pickle", "rb") as f:
# 	print(pickle.load(f))


# s = "hallo verden"
# c = " "
# print(c.join(s.split(c)))
# def group_sum(l):
#     d = {}
#     for pair in l:
#         d[pair[0]] = d.get(pair[0], 0) + pair[1]
#     return d


# # Example input and output
# data = [('A', 3), ('B', 5), ('A', 2), ('B', 1), ('C', 4)]
# print(group_sum(data))
# Expected output: {'A': 5, 'B': 6, 'C': 4}
s = "123,  41, 14,"
text = "     Hello World    "
l = []

print(s.replace(",", " ").split())


l = [1, 2, 3, 4]
a = ["a", "b", "c", "d"]
print(*zip(l, a))
