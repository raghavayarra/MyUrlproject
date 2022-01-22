# classes and objects
'''
class Person:
    pass

#instance object

p1=Person()
p2=Person()
print(p1)
print(p2)
print(id(p1))
print(id(p2))


class Person:
    def display(self):
        print("I am a Person")

    def greet(self):
        print("Hello, how are you doing??")

p1=Person()
p2=Person()

p1.display()
p1.greet()

p2.display()
p2.greet()

'''

'''
class Person:

    def set_details(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("I am ",self.name)

    def greet(self):
        if self.age<80:
            print("Hello, how are you doing??")
        else:
            print("hello,how do you do")
        self.display()

p1=Person()
p2=Person()
p1.set_details('raghava',25)
p2.set_details('ram',24)

p1.greet()
p2.greet()

# Excerise

class BankAccount:
    def set_details(self,name,balance=0):
        self.name=name
        self.balance=balance
    def display(self):
        print(self.name,self.balance)

    def withdraw(self,amount):
        self.balance=self.balance-amount
    
    def deposit(self,amount):
        self.balance=self.balance+amount

a1=BankAccount()
a1.set_details('Raghava',2000)

a2=BankAccount()
a2.set_details('kiran')

a1.display()
a2.display()

a1.withdraw(1000)
a2.deposit(500)

a1.display()
a2.display()


# __init__ method

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("I am ",self.name)

    def greet(self):
        if self.age<80:
            print("Hello, how are you doing??")
        else:
            print("hello,how do you do")
        self.display()

p1=Person('virat',30)
p2=Person('rahul',26)

p1.greet()
p2.greet()

'''
# Data Hiding

'''
class Product:
    def __init__(self):
        self.data1=10
        self._data2=20
    
    def method1(self):
        pass
    def _method2(self):
        pass

p=Product()
p.method1()
print(p.data1)
p._method2()
print(p._data2)
'''

class Product:
    def __init__(self):
        self.data1=10
        self.__data2=20
    
    def method1(self):
        pass
    def __method2(self):
        pass

p=Product()
p.method1()
print(p.data1)
p.__method2()
print(p.__data2)

