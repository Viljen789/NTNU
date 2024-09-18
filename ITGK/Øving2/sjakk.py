print(f"Ruten {(pos:=input("Hvilken rute ønsker du å vite fargen på?: "))} er {(int(pos[1])+(ord(pos[0])-ord("a")))%2*"sort" + (1-((int(pos[1])+int(ord(pos[0])-ord("a")))%2))*"hvit" }")

