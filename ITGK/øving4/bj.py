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
    "A": 11,
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


def trekk() -> str:
    sorter = ["\u2663", "\u2665", "\u2666", "\u2660"]
    verdier = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    kort = sorter[randint(0, len(sorter) - 1)] + verdier[randint(0, len(verdier) - 1)]
    return kort


def blackjack() -> float:
    dealer = []
    print("Dealeren trekker: ")
    dealersum = 0
    kort = trekk()
    animation()
    print(kort)
    dealersum += skib[kort[1:]]
    dealer.append(kort)
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
                trk = 0
                break
        kort = trekk()
        animation()
        print(kort)
        ps += skib[kort[1:]]
        hand.append(kort)
        if kort[0] == "A":
            ess = 1
        if(ess and ps>21):
            ps-=10
            ess = 0
        if(tottrekk == 1 and ps==21):
            print("Blackjack!")
            return 1.5

        if(ps>21):
            print("Du bustet :(")
            return -1
            trk = 0
        tottrekk += 1

    kort = trekk()
    animation()
    dealersum += skib[kort[1:]]
    dealer.append(kort)
    print(f"Dealeren snur en {kort}, og har nå {" ".join(dealer)}, som gir en sum på {dealersum}")
    while(dealersum<16):
        print(f"Dealeren snur {kort}, og har nå {" ".join(dealer)}, som gir en sum på {dealersum}")
        if(dealersum<16):
            print("Dealeren trekker ett nytt kort: ")
            kort = trekk()
            animation()
            print(trekk())
            dealersum += skib[kort[1:]]
            dealer.append(kort)
            time.sleep(1)

        if(dealersum>21):
            print("Dealeren bustet, og du vant!")
            return 1
    if(dealersum<ps):
        print(f"Du har hånden {" ".join(hand)} med en sum på {ps}, og slår derfor dealerens {dealersum}!")
        return 1

    elif(dealersum>ps):
        print(f"Du har hånden {" ".join(hand)} med en sum på {ps}, og taper derfor mot dealerens {dealersum}!")
        return -1

    else:
        print(f"Du har hånden {" ".join(hand)} med en sum på {ps} mot dealerens {dealersum}, og det blir derfor push (uavgjort)!")
        return 0


cont = True
balance = 1000
bet = 0
valid = 1
edgingstreakmogginglooksmaxonjohnporkrizzmewingstreak = 1
while cont:
    while valid:
        bet = int(input(f"Hvor mye vil du satse? (0-{balance})$ "))  
        if bet == 0:
            cont = 0
            valid = 0
            edgingstreakmogginglooksmaxonjohnporkrizzmewingstreak = 0
            break

        if bet <= balance:
            print(f"Satser {bet}$ ...")
            break
        else:
            print("Du har desverre ikke nok")
    if edgingstreakmogginglooksmaxonjohnporkrizzmewingstreak:
        balance += bet*blackjack()

