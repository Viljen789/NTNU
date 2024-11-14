import pickle 


l = [x for x in range(2, 100) if all(x%p!=0 for p in range(2, x))]

with open("prim.pickle", "wb") as f:
    pickle.dump(l,f)

with open("prim.pickle", "rb") as f:
	print(pickle.load(f))

pickle.