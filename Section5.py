# if and else Statement.

lastball =int(input("enter the number :"))

if lastball==6:
    print("won the match")

else:
    print("loss the match")


# even or odd

number = int(input("Enter a number :"))
if number%2==0:
    print(number,"is Even number")
else:
    print(number,"is odd number")


# Nested if

item ="fruits"
fruit ="apple"
if item =="fruits":
    if fruit == "apple":
        print("This fruit is an apple")
    else:
        print("This fruit is not avaliable")

else:
    print("This is not a fruit")