#print("Hello world!!")

# variables
'''age = 20
print(age)

sentence="My name is raghava"
print(sentence)

# multiple assignment
raghava,kiran,ram=16,21,17
print(kiran)

raghava=kiran=mike=17

print(ram)

# create name & age using multiple assignment

name,age="raghava",27
print(name)
print(age)'''


# Operations & strings

# Arithmetic Operators:
'''a = 10.5
b=2
# Addition
print('a+b=',a+b)
# Subtraction
print('a-b=',a-b)
# Multiplication
print('a*b=',a*b)
# Division operator
print('a/b=',a/b)
# Floor Division operator
print('a//b=',a//b)
# Modulo operator
print('a%b=',a%b)
# Exponent operator or power operator
print('a**b=',a**b)'''


#strings

'''firstname="raghava"
lastname ="yarra"
print(firstname+lastname)
print(firstname+" "+lastname)
print("Hello" *10)'''

#multi-line String literals
s='''learning 
python is 
very
easy'''
'''print(s)

# access characters of a String:

# By using index
s="learning python is very Easy"
print(s[4])
print(s[-2])

# By using slice operator

s="learning python is very Easy"
print(s[1:7])
print(s[::-1])
'''
#len()

'''s="raghava"
print(len(s))
# access each character of string in forward and backward direction by using while loop.
i=0
n=len(s)
print("Forward direction :")
while i<n:
    print(s[i])
    i=i+1

print("backward direction :")

i=-1
while i>=-n:
    print(s[i])
    i=i-1

s="Learning Python is very easy !!!"

for x in s:
    print(x,end="")

print("Backend")
for x in s[::-1]:
    print(x,end="")


#Checking Membership:

s="raghava"
print("h" in s)
print("y" not in s)


s="raghava"
print(s.find("y"))
print(s.index("h"))

# Placeholder
name = " rohit"
print(name+" is 15 years old")

sent= "%s is 15 years old"
print(sent)
print(sent%name)

print(sent%("ravi"))

sent="%s %s is the president of the US"
print(sent%("Barack","Obama"))

sent="%s is %d years old"
print(sent%("ravi",27))

'''
#list
'''list =[10,10.5,True,"raghava"]
print(list)
print(list[3])
list[0]=25
print(list)
for i in list:
    print(i)

list.append("kiran")
print(list)
list.insert(1,1000)
print(list)
list.extend([10,20,30])
print(list)

del list[0]
print(list)
l1=[10,20,30,70,80,14]
print(max(l1))
print(min(l1))

'''

# Dictionaries:-

'''students={'kiran':12,'ramesh':13,'virat':15}
print(students)
print(students['kiran'])

#update the dict
students['virat']=25
print(students)

# delete the dict
del students['ramesh']
print(students)

#len 
print(len(students))'''


# Tuples:-
'''
t=("oranges","apples",'grapes')
print(t)
print(t[1])
print(t[:2])
t1=(20,30)
t2=t+t1
print(t2)

print(len(t2))
'''

#conditional statements

'''name=input("Enter Name:")
if name=="virat" :
    print("Hello virat Good Morning")
else:
    print("Hello Guest Good Moring")
    print("How are you!!!")'''


'''city = input("enter a city: ")

if city == "hyd":
    print("welcome to hyd")
elif city == "Ap":
    print("welcome to Ap")
elif city == "Ts":
    print("welcome to Ts")

else:
    print("please enter valid city name")'''

'''a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter Third number :"))

if a>b and a>c:
    print("a is bigger number",a)
elif b>c:
    print("b is bigger number ",b)
else:
    print("c is bigger number",c)

'''

# For loops:-
'''
list=['Apple','grapes','cherries']
for item in list:
    print(item)

t=(10,20,30,40)
for x in t:
    print(x)

# even numbers
for i in range(0,20,2):
    print(i)
'''

# While loops:-
'''

s="kiran"
i=len(s)-1
target=""
while i>=0:
    target=target+s[i]
    i=i-1
print(target)

# break

i=0
while i<10:
    print(i)
    if i==7:
        break
    i=i+1

# continue 
i=0
while i<10:
    i=i+1
    if i==7:
        continue
    print(i)
    
#Pass
i=0
while i<10:
    i=i+1
    if i==7:
        pass
    print(i)


# Try and Except:-
try:
    if name >3:
        print("Hello")
    
except:
    print("There is something wrong with your code please check again")
'''

# Functions:-

'''def wish(name):
    print("Hello",name," Good Morning")
wish("ram")
wish("Ravi")


def add(x,y):
    return x+y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))


# In-Built Functions

print(abs(-20))
print(bool(0))
print(bool(1))
print(dir("hello"))

'''

# OOPs:-

class Person:
    pass
p=Person()
print(p)

class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):
        print("Hello My Name is:",self.name)
        print("My Rollno is:",self.rollno)
        print("My Marks are:",self.marks)

s1=Student("Ram",25,90)
s1.talk()

# Inheritance:-


class Parent:
    def __init__(self):
        print("This is the parent class")
    
    def parentFunc(self):
        print("This is the parent func")

p=Parent()
p.parentFunc()

class Child(Parent):
    def __init__(self):
        print("This is the child class")
    
    def childFunc(self):
        print("This is the child func")



c=Child()
c.childFunc()
c.parentFunc()


# over writing


class Parent:
    def __init__(self):
        pass
    
    def test(self):
        print("parent")



class Child(Parent):
    def __init__(self):
        pass
    
    def test(self):
        print("Child")


c=Child()
c.test()