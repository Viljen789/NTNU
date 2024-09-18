while True:
    hid = input("Hemmelig ord: ")
    for i in range(20):
        print("*" * 100)
    liv = int(input("Antall liv:"))
    sol = []
    for i in range(len(hid)):
        sol.append("-")
    boks = 0
    tidl = []
    while liv > 0:
        print(f"Hemmelig ord: {''.join(map(str, sol))}, og du har {liv} liv igjen")
        gjett = input("Gjett: ")
        bom = 1
        if (gjett == hid):
            print(f"Korrekt! Du klarte det med {liv} liv igjen!")
            liv = 0
        if gjett in tidl:
            print("Alerede gjettet, velg en ny: ")
            continue
        for i in range(len(hid)):
            if hid[i] == gjett:
                sol[i] = gjett
                boks += 1
                bom = 0
        liv -= bom
        if bom:
            print(f"Feil, det er ingen {gjett} i ordet")
        else:
            print(f"Korrekt, {gjett} er i ordet")
        tidl.append(gjett)
        if boks == len(sol):
            print(f"Korrekt! Du klarte det med {liv} liv igjen!")
            liv = 0
    fort = input("Fortsette? (J/N)")
    if fort.lower() == "n":
        break
