import csv
with open('poenggrenser_2011.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='"')
    d = {}
    retning = {}
    for(row) in data:
        uni = row[0].split()[0]
        res = {}
        if(uni not in d):
            d[uni] = []
        d[uni].append({row[0].split()[1]:row[1]})


for key in d:
    print(key)
    for i in d[key]:
        print(" "*5 , i)
    print("\n")










