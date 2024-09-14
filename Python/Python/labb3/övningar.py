import numbers

numbers = {"one":1, "two":2, "seven":6, "eight":9}
numbers["three"] = 3
numbers["eight"] = 8

print(numbers)
'''
coordinates_one = { (1,0,0): "x-axis", (0,1,0): "y-axis"} #Funkar den under funkar ej
coordinates_two = { [1,0,0]: "x-axis", [0,1,0]: "y-axis"}
print(coordinates_one)
'''

pos_one = {"x":5,"y":0}
pos_two = {"x":'fem',"y":'noll'}
pos_three = {"x":[5],"y":[0]}

pos_one["y"]=5
'''
print("(",pos_one["x"], ",",pos_one["y"],")") 

print(pos_one["x"])
print(pos_two["x"])
print(pos_three["x"])
'''

def power(x,y):
    result = 1
    for i in range(y):
        resultat *= x
    return result

def sum_first(n):
    if n==0:
        return 0
    else:
        return n + sum_first(n-1)
    
#print(sum_first(6))
    
def is_number(x):
    return isinstance(x, numbers.Number)

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))