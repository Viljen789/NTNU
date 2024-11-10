from datetime import datetime
def current_date():
    yyyy = int(datetime.today().strftime('%Y'))
    mm = int(datetime.today().strftime('%m'))
    dd = int(datetime.today().strftime('%d'))
    return yyyy,mm,dd

def findAge(bYear, bMonth, bDay):
    shift = 0
    y, m, d = current_date()
    if(bMonth>m or (bMonth==m and bDay>dd)):shift = -1
    return y- bYear + shift
age = findAge(2000,7,15)
print(age)
table=[['Justin','Bieber',1994,3,1],
       ['Donald','Duck',1934,8,1],
       ['George','Clooney',1961,5,6],
       ['Eddie','Murphy',1961,4,3]]

def printAgeDiff(table):
    for i in range(len(table)-1):
        for j in range(i+1,len(table)):
            age1 = findAge(table[i][2],table[i][3],table[i][4])
            age2 = findAge(table[j][2],table[j][3],table[j][4])
            print(table[i][0],table[i][1],'is',age1,'years older than',table[j][0],table[j][1])
            print(table[j][0],table[j][1],'is',age2,'years younger than',table[i][0],table[i][1])
            print()

printAgeDiff(table)

def fu3(a):
    if(a<=2):
        r = 1
    else:
        r = 1 + fu3(a/2)
    return r

print(fu3(100))    
for i in range(0,10):
    print(i, 2**i)

def generate_testdata(N, mmin, mmax):
    return [random.randint(mmin,mmax) for i in range(N)]


def create_db(temp, rain, humidity, wind):
    d = {}
    for i in range(len(temp)):
        d[i] = (temp[i], rain[i], humidity[i], wind[i])

    return d;

def print_db(d):
    for i in d:
        print(i, d[i])




def strange_weather(temp, rain):
    if(len(temp) == 0):return (0,0)
    start = 0
    stop = 0
    for i in range(len(temp)-1):
        if(temp[i]<0 and temp[i+1]<temp[i] and rain[i+1]>rain[i]):
            start = i+1
            stop = i+2
    return (start,stop)
