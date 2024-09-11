bday_colin = 920 # colin
bday_felix = 821 # felix
bday_hugo= 518 # hugo
bday_max= 506 # max
bday_viggo = 413 # viggo
print("Skriv in Datumet i formatet mmdd")
x=int(input())

def bday(x):
    if x > bday_colin:
        return str(x) + " Fyllde Colin år senast"
    elif x > bday_felix:
        return str(x) + " Fyllde Felix år senast"
    elif x > bday_hugo:
        return str(x) + " Fyllde Hugo år senast"
    elif x > bday_max:
        return str(x) + " Fyllde Max år senast"
    elif x > bday_viggo:
        return str(x) + " Fyllde Viggo år senast"
    else: return "Ingen har fyllt än i år"




print(bday(x))


























def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a



def gcd2(a,b): #sats
    if b==0: # sats samansats sasts
        return a #sats
    else: 
        return gcd2(b,a%b) #sats, sammansat sats + samansat sats

    #print(gcd2(148,2622))











def fibonacci(n): #sats
    if n < 3: #sammansatt + Sats   N<3
        return n-1 #sammansatt + Satts
    a = 0 #sats tilldelningssatts
    b = 1 #sats

    for i in range(n - 2): #SAMMANSATT + Satts
        previous_number = b #sats
        b = a + b #sats SAMMANSATT
        a = previous_number #sats
    return b #Sammansatt + sats
#1. räknar fibonacci sekvensen, håller ett temporärt värde för det talet innan det man räknar ut. Previous_number,
#  Int, Error "Float" object cannot be interpreteded as an interger. Då in range inte funkar med floats
#container för värdet på c för att det barra är en container som räknar. container, save, temp


#5 tilldelnigns sattser
# 2 retur satser
# Sats för For, If och funktionen
# Sammansatta n-1, a+b, n-2, n<3, range(n-2)




#print(fibonacci(5.2))
#0 0 1 1 2 3






g = 0
def outer(in1):
    a = "a"
    def inner(in2):
        print(a) # 1.
        c = "c"
        a = "a from inner"
        print(in2) # 2.

    print(c) # 3
    print(a) # 4

    inner("into inner")

    print(c) # 5

    print(a) # 6

    if g == 0:
        d = "g = 0"
    else:
        e = "g != 0"

    print(d) # 7.
    print(e) # 8



























def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a



def gcd2(a,b): #sats
    if b==0: # sats samansats sasts
        return a #sats
    else: return gcd2(b,a%b) #sats, sammansat sats + samansat sats

    #print(gcd2(148,2622))











def fibonacci(n): #sats
    if n < 3: #sammansatt + Sats   N<3
        return n-1 #sammansatt + Satts
    a = 0 #sats tilldelningssatts
    b = 1 #sats

    for i in range(n - 2): #SAMMANSATT + Satts
        previous_number = b #sats
        b = a + b #sats SAMMANSATT
        a = previous_number #sats
    return b #Sammansatt + sats
#1. räknar fibonacci sekvensen, håller ett temporärt värde för det talet innan det man räknar ut. Previous_number,
#  Int, Error "Float" object cannot be interpreteded as an interger. Då in range inte funkar med floats
#container för värdet på c för att det barra är en container som räknar. container, save, temp


#5 tilldelnigns sattser
# 2 retur satser
# Sats för For, If och funktionen
# Sammansatta n-1, a+b, n-2, n<3, range(n-2)




#print(fibonacci(5.2))
#0 0 1 1 2 3






g = 0
def outer(in1):
    a = "a"
    def inner(in2):
        print(a) # 1.
        c = "c"
        a = "a from inner"
        print(in2) # 2.

    print(c) # 3
    print(a) # 4

    inner("into inner")

    print(c) # 5

    print(a) # 6

    if g == 0:
        d = "g = 0"
    else:
        e = "g != 0"

    print(d) # 7.
    print(e) # 8.