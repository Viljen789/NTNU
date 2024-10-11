from time import sleep
def board(l:list):
    print("""
    
    
      -------------
      | {} | {} | {} |
      -------------
      | {} | {} | {} |
      -------------
      | {} | {} | {} |
      -------------
      """.format(str(l[0])+" "*(1-len(str((l[0])))), str(l[1])+" "*(1-len(str((l[1])))), str(l[2])+" "*(1-len(str((l[2])))), str(l[3])+" "*(1-len(str((l[3])))), str(l[4])+" "*(1-len(str((l[4])))), str(l[5])+" "*(1-len(str((l[5])))), str(l[6])+" "*(1-len(str((l[6])))), str(l[7])+" "*(1-len(str((l[7])))), str(l[8])+" "*(1-len(str((l[8]))))))

def check(l):
    for i in range(3):
        if(l[i]== l[i+3] and l[i]==l[i+6] and l[i]!= " "):return l[i]
        if(l[i*3]== l[i*3+1] and l[i]==l[i*3+2]and l[i]!= " "):return l[i]
    if(((l[0]==l[4] and l[4]==l[8]) or (l[2]==l[4] and l[4]==l[6]))and l[4]!= " "):return l[4]
    draw = 1
    for i in range(9):
        if(l[i]==" "):draw = 0
    if(draw):return -1
    return 0

def navn():
    f = input("Navn til spiller 1: ")
    s = input("Navn til spiller 2: ")
    return f, s

def lovlig(l, p):
    return l[p]==" "

def valid(l, p):
    return p<9 and p>=0 and l[p]==" "

def positions():
    print("""
    
    
    
Feltene på brettet har følgende index:
        -------------
        | 1 | 2 | 3 |
        -------------
        | 4 | 5 | 6 |
        -------------
        | 7 | 8 | 9 |
        -------------
""")

players = [0]*2
players[0], players[1] = navn()
mark = ["x", "o"]
l = [" "]*9
turn = 1

print(f"{players[0]} spiller som x, {players[1]} spiller som o")
sleep(3)
positions()
sleep(3)

while 1:
    while not check(l):
        board(l)
        val = 1
        while(val):
            p = input(f"{players[turn%2]} sin tur: \nHvor vil du legge briken din? (1-9)")
            try:
                p = int(p)-1
                val = 0
            except:
                print("Posisjonen må vere ett tall mellom 1-9")
        while not valid(l, p):
            val = 1
            while(val):
                p = input(f"{players[turn%2]} sin tur: \nHvor vil du legge briken din? (1-9)")
                try:
                    p = int(p)-1
                    val = 0
                except:
                    print("Posisjonen må vere ett tall mellom 1-9")
        turn +=1
        l[p]=mark[turn%2]
    board(l)
    if(check(l)==-1):print("Uavgjort!")
    else: print(f"Gratulerer {(players[mark.index(check(l))]+1)%2}")
    cont = input("Vil du spille igjen? (y/n)")
    if cont.lower()!= "y":break

