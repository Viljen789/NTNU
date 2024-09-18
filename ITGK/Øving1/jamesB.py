# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 5
# Oppgi ønsket antall desimaler i avrunding: 0
# 2.5 avrundet til 0 desimaler blir 2
num = str(float(input("desimaltall: ")))
komma = num.find(".")
intdel = num[:komma]
desdel = num[komma+1:]
presisjon = int(input("Hvor mange desimaler?"))
# print(intdel)
# print(desdel)
# Antar at alltid vil runde av bak komma

if(presisjon<=0):
    print(round(intdel, presisjon)) + (int(desdel[0])>5)
else:
    print(f"{intdel}.{round(int(desdel), presisjon-len(desdel)):.f}")