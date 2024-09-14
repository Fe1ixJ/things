def div_by_three(n):
    div = n/3
    print(div)
    return div % 1==0
    
def max2(x,y):
    
    if x>y:
        return x
    else:
        return y
    
def max3(x,y,z):
    return max2(max2(x,y),z)
    
print(div_by_three(61))
max=max3(10,4,6)+max2(4,3)
print(max)

#Print och return
#Redovisa på fredag