f = open("datafil.txt", "w")
f.write("""3 ; 2.5 ; 3.5 ; Alta
1 ; 0.25 ; 1.0 ; Tana
2.0 ; 1 ; 1.0 ; Hamar
5 ; 7 ; 3 ; Oslo""")

def respons(fil, r, c):
    try:
        with open(fil) as f:
            line = f.readlines()[r].split(";")
            if not c:
                return line[3].strip()[int(line[c])]
            else:
                return float(line[c])
    except FileNotFoundError:
        return -1
    except:
        return -2

d = "datafil.txt"
t = "tallfil.txt"


print(respons(d, 3, 0))

