str1 = "iS"
str1 = str1.lower()
str2 = "Is this the real life? Is this just fantasy?"
str2 = str2.lower()
str3 = "cool"

i = len(str1)
while(i<len(str2)):
    if(str1==str2[i-len(str1):i]):
        str2=str2[:i-len(str1)] + str3 + str2[i:]
    i+=1
        

        

print(str2)

def swap(a, b):
    return b, a

