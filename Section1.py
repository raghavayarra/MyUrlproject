class Person:
    pass
id(Person)
p1=Person()
p2 = Person()
print(p1)
print(p2)


class Person:
    def display(self):
        print('I am a person')
    def greet(self):
        print('Hello, how are you doing?')

p1=Person()
p1.display()
p1.greet()

p2 = Person()
p2.display()
p2.greet()


class Person:
    def diaplay(self):
        print('I am a person', self)
    def greet(self):
        print('Hi, how are you doing ? ', self)

p1=Person()
p1.name ="Tom"
print(p1.name)


class Person:
    def set_details(self):
        self.name = 'John'
        self.age = 20
    def display(self):
        print('I am a person', self)
    def greet(self):
        print('Hi, how are you doing ? ', self)

p1=p2=Person()
p1.set_details()
p2.set_details()
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


p2.name ='Jack'
p2.age = 30

print(p2.name)
print(p2.age)


class Person:
    def set_details(self,name,age):
        self.name = 'John'
        self.age = 20
    def display(self):
        print('I am ', self.name)
    def greet(self):
        if self.age < 80:
            print('Hi, How are you doing?')
        else:
            print('Hello, How do you do?')
        self.display()

p1=Person()
p1.set_details('Bob', 20)
p1.greet()
p2=Person()
p2.set_details('Ted', 90)
p2.greet()