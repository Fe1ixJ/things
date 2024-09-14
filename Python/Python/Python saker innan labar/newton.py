def find_root(): #Funktionsdefinition
    print("This program tries to find the root of your number") #Funktionsanrop
    x = eval(input("Enter a numbe: ")) #Eval kör rakt i terminalen och får då t.ex en 3 och den märker då att det är int 3 vilket blir livsfarligt då användare får skriva rakt in i terminalen
    #input plockar från consol
    guess = x/2 #Tilldelar och då blablabla name=utryck
    for i in range (100000): #Iteration sats körs så många ggr som det specificerar
        guess = (guess + x/guess)/2 #tilldelar
        if i == 5: #Selektion med IF. Gör detta eller detta beroende om sant eller inte. ELIF = Elseif?
            print(guess) #Funkanrop
    print(guess) #Funktionsanrop

find_root() #Funktionsanrop. Parantesen måste vara med även utan angrument.