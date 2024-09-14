def find_root():
    print("This program tries to find the root of your number")
    x = eval(input("Enter a number: ")) # Eval gör om string to int. Eval är farligt EVIL IS EVIL. Tar text och låsats att det är python terminalen som tänker som den och får ut värdet. Input hämtar info från användaren i terminalen. Enter kör programet igen. 
    #Eval kan ge användaren kontrollen att köra var den vill i programmet vilket kan bli farligt och osäkert
    guess = x/2
    for i in range (10000000): # Göra 5 ggr upp 0-4
        guess = (guess + x/guess)/2
        if i ==5:
            print("Efter + 5 försök " + guess)
    print("Efter MÅNGA försök " + guess)

find_root()

#GRÖNT
'''
import math

x = eval(input("Enter a number: "))
y= math.sqrt(x)
print(y)
'''