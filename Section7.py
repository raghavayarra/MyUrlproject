# User defined Functions

def wish():
    print("Hi..gud eveng")

wish()
wish()

# Write a function to take number as input and print its square value.
def squareIt(number):
    print("The Square of",number,"is", number*number)
number=int(input("enter a number: "))
squareIt(number)

# Variable length arguments.

def sum(*args):
    total=0
    for x in args:
        total=total+x
    print("The sum is :",total)

sum(10)
sum(10,20)
sum(10,20,30)
