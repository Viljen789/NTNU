# from math import sqrt, ceil
# p = int(input("Skriv inn ett positivt heltall: "))
# org = p
# l = []
# i = 2
# while(p>1 and i<(org/2)):
#     while(p%i==0):
#         l.append(i)
#         p/=i
#     i+=1
# if(len(l)==0):
#     print("Primtall")
#     exit()
# print(org, "= ", end = "")
# for i in range(len(l)-1):
#     print(l[i], end = " * ")
# print(l[-1])


def SOE(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:

        if prime[p] == True:

            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    print(prime[-1])


num = int(input("Tall: "))
SOE(num)
