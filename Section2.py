# property

class Product:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def display(self):
        print(self._x,self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self,val):
        self._x=val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,val):
        self._y=val


p=Product(12,24)

p.display()
print(p.value)
p.value=19
print(p.value)

p.y=20
print(p.y)






class Person:
    def __init__(self,name,age):
        self.name =name
        self._age=age
    
    def display(self):
        print(self.name,self._age)

    def set_age(self,new_age):
        if 20<new_age<80:
            self._age = new_age

        else:
            raise ValueError('Age must be between 20 and 80')

    def get_age(self):
        return self._age


if __name__ == "__main__":
    p=Person('kiran',30)

p.display()
p.set_age(50)
print(p.get_age())


# by using property


class Person:
    def __init__(self,name,age):
        self.name =name
        self.age=age

    def display(self):
        print(self.name,self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,new_age):
        if 20<new_age<80:
            self._age=new_age
        else:
            raise ValueError('Age muust be between 20 and 80')

if __name__ == "__main__":
    p=Person('Raghava',25)
    p.display()

    p.age=100
    