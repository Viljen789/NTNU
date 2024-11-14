n = 10

def dtb(n):
    n = int(n)
    ans = ""
    while(n):
        if(n&int(1)):ans+="1"
        else:ans+="0"
        n//=2
    return ans[::-1]

print(dtb(n))
