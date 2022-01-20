
# indexing

from turtle import color


animals=["dog","cat","lion","tiger"]
print(animals)
print(animals[1])
print(animals[-1])


#slicing

list=[0,1,2,3,4,5,6,7,8,9]
print(list[2:8])
print(list[-5:-1])
print(list[:])
print(list[:5])
print(list[::-1])

#Sequences

a=[0,1,2,3]
b=[4,5,6,7]
print(a+b)


name=input("enter a name: ")

print("k" in name)
print("r" in name)


# More operations on Sequence and Lists

numbers=[21,30,51,87,65,40]
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers[2]=999
print(numbers)

# methods

colors =['red','green','yellow']

colors.append("yellow")
print(colors)
colors.insert(1,"blue")
print(colors)
colors.extend(numbers)
print(colors)

numbers=[1,1,2,2,3,3,3,4,5]
print(numbers.count(1))

# write a program in python which finds a letter in a string.
# Ex:- string = "Example String",letter = "S" returns True.

s=input("Enter main string : ")
sub=input("Enter sub string: ")
if sub in s:
    print(sub," is found in main string")
else:
    print(sub," is not found in main string")

# write a program in python to reverse a string using slicing method.
# ex:- string="helloworld",returns reversed string="dlrowolleh"

string=input("enter a  string : ")
s=string[::-1]
print("Reversed string: "+s)


