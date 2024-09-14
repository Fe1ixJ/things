def choose(n,k):
    värde_n=factorial(n)
    värde_k=factorial(k)
    värde_nk=factorial(n-k)
    return värde_n/(värde_k*värde_nk)


def factorial2(n):
    resultat = 1
    for i in range(n):
        resultat *= n-i
    return resultat

#REKURSION
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(choose(1000,800))

#print(factorial2(1000))  
#print(choose(1000,800))






#Rekursivt skriv ut exempel och hitta sätt att förenkla det på 
#Symetri i biminolsatsen
#Chooose i coose och itne använda factorial för är ligger problemet