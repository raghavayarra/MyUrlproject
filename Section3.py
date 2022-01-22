# Inheritance

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  


#Multiple inheritance

class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Calculation1,Calculation2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))


# polymorphism
class Duck:
    def talk(self):
        print('Quack.. Quack..')
class Dog:
    def talk(self):
        print('Bow Bow..')
class Cat:
    def talk(self):
        print('Moew Moew ..')
class Goat:
    def talk(self):
        print('Myaah Myaah ..')
def f1(obj):
    obj.talk()

l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)