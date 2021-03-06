def gcdRecur(a,b):
    '''
    a and b are integers
    returns greatest common denominator 
    '''
    gcd = max(a,b) % min(a,b)
    if gcd == 0:
        return min(a,b)
    if min(a,b) % gcd == 0:
        return gcd
    return gcdRecur(gcd,min(a,b))
def popList (x,y,z=1):
    '''
    returns every integer between x and y
    z = skip numbers
    '''
    l = []
    if x > y:
        x,y = y,x
    while x <= y:
        if i not in l:
            l.append(x)
        x += z
    return l
        
def leastCommonMultiple (a,b):
    '''
    find LCM between 2 numbers
    '''
    return (a/gcdRecur(a,b))*b
x = 1
y = 20
z = 1
i = 0
l = popList(x,y,z)
while i < len(l)-1:
    x = (leastCommonMultiple(l[i], x))
    i += 1
print(int(x))

