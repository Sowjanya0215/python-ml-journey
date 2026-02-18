#factorial -----

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
        print(fact)
fact(5)
def pro(a,b):
    print(a*b)
    return a*b
pro(2,8)

#converter-----

def converter(usd_value):
    inr=usd_value*83
    print(usd_value,"usd",inr,"inr")
converter(2) 

#even or odd-----

def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(evenodd(4)) 

#maximum of three------

def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
print(max(2,3,4)) 

#prime number-----

def prime(z):
    if z <= 1:
        return False
    
    for i in range(2, int(z**0.5) + 1):
        if z % i == 0:
            return False
    
    return True

print(prime(6))



  
