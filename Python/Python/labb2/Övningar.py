import numbers
import math

def unit(x):
    digit = x % 10
    return digit

def ten(x):
    digit = x//10 % 10
    return digit

def swap_unit_ten(x):
    first_digit = x//100
    digit = first_digit*100 + ten(x)*10 + unit(x)
    return digit

def power(x,y):
    return x**y

def power2(x,y):
    resultat = 1
    for i in range(y):
        resultat *= x
    return resultat

print(power2(2,4))
    
def sum_first(x):
    variable=(x(x+1))/2
    return variable

def sum_number(lista):

    total = 0
    for item in lista:
        if isinstance(item, (int, float)):
            total += item
    return total

lista = [2, 5, 2, 6, 2, "a"]
#print(sum_number(lista))

def find_letter(x, lista):
    if x in lista:
        return "True"
    else:
        return "False"


    
    
'''
lista2 = ["a","b","f", "k", "o"]
lista3 = ["a","b", "k", "o"]
print(find_letter("f",lista2))
print(find_letter("f",lista3))
'''

def remove_vowels(lista):
    total = []
    for item in lista:
        if item not in vowels:
            total += [item]
    return total

lista4= ["a", "b", "o", "k", "f", "i"]
vowels= ["a","o","u","å","e","i","y","ä","ö"]
print(remove_vowels(lista4))


