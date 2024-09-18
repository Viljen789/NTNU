l = []
name = input("Navn: ")
l = name.split(" ")
suffix = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "Jr", "Sr", "sr", "jr"]
prefix = ["Von", "Van", "De", "Di"]
last = l[-1]
if(l[-1]in suffix):
    last = l[-2]
    if(len(l)>2):
        if(l[-3]in prefix):
            last = l[-3]
            last +=" "
            last +=l[-2]
            
if(l[-2]in prefix):
    last = l[-2]
    last +=" "
    last +=l[-1]

print("My name is ", last)
print(name)