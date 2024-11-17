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

add("Viljen", 1)
add("Benjamin", 2)
read("Benjamin")
kontakter()
add("Børge", 3)
kontakter()

print(k := 3)
print(k)

#v = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
#vector<vector<int>> v = 