# oops:-

class calculator:
    def add(self,a,b):
        return a+b
    
    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b

calc= calculator()
result = calc.add(5,2)
print(result)

result = calc.sub(5,2)
print(result)
result = calc.mul(5,2)
print(result)


# Extended classes and methods

class A:
    var1="I am class A"

class B:
    var2="I am class B"

class C(A,B):
    var3="I am class C"

x=C()
print(x.var1)
print(x.var2)
print(x.var3)

