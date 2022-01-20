# Modules and Functions in Python:-

import math
print(math.sqrt(81))
print(math.factorial(5))

# write a program in python which returns the gcd of two numbers.

print("The gcd of 9 and 15 is : ", end="")
print(math.gcd(9,15))


def computeGCD(a,b):
    if b==0:
        return a
    
    else:
        return computeGCD(b,a%b)

a=int(input("enter a first number :"))
b=int(input("enter a second number :"))

print(computeGCD(a,b))


# write a program in python which calculates the LCM of two numbers.

def Compute_LCM(n1,n2):
    if n1>n2:
        higher = n1
        
    else:
        higher = n2
    
    value =higher

    while True:
        if higher%n1==0 and higher%n2==0:
            print("LCM of {} and {} is {}".format(n1,n2,higher))
            break

        else:
            higher=higher+value
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

Compute_LCM(n1,n2)


