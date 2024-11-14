import pickle

d = {}
with open("kontakt.pickle", "wb") as f:
		pickle.dump(d, f)

def add(navn, num):
	with open("kontakt.pickle", "rb") as f:
		d = pickle.load(f)
	d[navn] = num
	with open("kontakt.pickle", "wb") as f:
		pickle.dump(d, f)

def kontakter():
	with open("kontakt.pickle", "rb") as f:
		d = pickle.load(f)
	print(*d.keys(), sep=", ")

def read(navn):
	with open("kontakt.pickle", "rb") as f:
		d = pickle.load(f)
	print(d[navn])

list 
add("Viljen", 1)
add("Benjamin", 2)
read("Benjamin")
kontakter()
add("Børge", 3)
kontakter()

