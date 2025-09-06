class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self .a< other.a):
            return "object 1 is less than object 2"
        else:
            return "object 1 is greater than object 2"
    def __eq__(self,other):
        if (self.a==other.a):
             return "object 1 is equal to object 2"
        else:
            return "object 1 is not equal to object 2"
            
obj1=A(2)
obj2=A(4)

print("passed values",obj1.a ,obj2.a)
print(obj1<obj2)

obj1=A(10)
obj2=A(10)

print('passed values',obj1.a ,obj2.a)
print(obj1 == obj2)

