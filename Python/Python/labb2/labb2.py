#personnummer = [0, 4, 0, 8, 2, 1, 3, 8, 1, 7]
weight = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]

def check_pnr(x,y):
    summ = 0
    for i in range(9): #Loppar för alla i siffror i person nr utom för kontroll siffran
        product =(x[i]*y[i]) #Multiplicerar ihop pn med weight för att få det viktade pn
        if product > 9:
            summ += product //10 #För att få tio siffran
            summ += product % 10 # För att få entalet.    Går inte att få störe siffror än 18 så därför behövs endast detta
        else:
            summ += product

    #För att avrunda upp till närmsta heltal
    kontroll = (summ//10+1)*10 - summ 
    #Checka kontroll siffra
    if kontroll == x[9]:
        return "True"
    else:
        return "False"
    
print("Skriv in ditt personnummer")
number=input()
digits = [int(digit) for digit in str(number)] # Convert the number to a string, loop through each character (digit), convert each character back to an integer, and store it in a list.
#print(digits)
print(check_pnr(digits, weight))