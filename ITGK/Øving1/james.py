num = str(float(input("desimaltall: ")))
presisjon = int(input("antall desimaler? "))
lok = num.find(".")
pos = lok+presisjon+1
if(presisjon<0):
    pos-=1
if(pos>=len(num)):
    print(f"Avrundet til {presisjon} desimaler: {round(float(num), presisjon)}")
else:
    newstr = num
    if(num[pos]=="5"):
        newstr = num[:pos] + "6" + num[pos+1:]
    print(f"Avrundet til {presisjon} desimaler: {round(float(newstr), presisjon)}")
