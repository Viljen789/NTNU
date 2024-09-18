import itertools
import threading
import time
import sys
from random import randint

done = False


def animation():
    animation = "|/-\\ ‘"

    for i in range(11):
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.07)

    sys.stdout.write("")


skib = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def dealersnu() -> str:
    done = True
    kort = trekk()
    animation()
    print(trekk())
    dealersum += skib[kort[1:]]
    return kort

def trekk() -> str:
    sorter = ["\u2663", "\u2665", "\u2666", "\u2660"]

    verdier = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    kort = sorter[randint(0, len(sorter) - 1)] + verdier[randint(0, len(verdier) - 1)]
    return kort


def blackjack(bet: int) -> float:
    dealer = []
    print("Dealeren trekker: ")
    dealersum = 0
    f = dealersnu
    dealer.append(f)
    animation()
    print("?")
    print("Du trekker ...")
    time.sleep(0.5)
    trk = 1
    ps = 0
    tottrekk = 0
    ess = 0
    hand = []
    while trk:
        if(tottrekk >1):
            print("Du har " + " ".join(hand))
            svar = input(f"Du har en sum på {ps}, vil du trekke ett kort til? (y/n)")
            if svar.lower()=="n":
                break
        kort = trekk()
        hand.append(kort)
        animation()
        print(trekk())
        ps += skib[kort[1]]
        if kort[0] == "A":
            ess = 1
        if(ess and ps>21):
            ps-=10
            ess = 0
        if(totrekk == 1 and ps==21):
            print("Blackjack!")
            return 1.5

        if(ps>21):
            print("Du bustet :(")
            return -1
            trk = 0
        tottrekk += 1

    f = dealersnu 
    dealer.append(f)
    
    print(f"Dealeren snur en {f}, og har nå {"".join(dealer)}, som gir en sum på {dealersum}")
    if(dealersum<ps){
        print(f"Du har hånden {"".join(hand)}, og slår derfor dealeren!")
        return 1
    }
    elif(dealersum>ps){
        print(f"Du har hånden {"".join(hand)}, og taper derfor mot dealeren!")
        return -1
    }
    else:
        print(f"Du har hånden {"".join(hand)}, og det blir derfor push (uavgjort)!")
        return 0

    


blackjack(10)
