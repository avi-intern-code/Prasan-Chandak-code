#  python does not support method overloading by default

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Trying method overloading in python using if-else
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a + b + c

        elif a!=None and b!=None:
            s = a+b

        else:
            s = a

        return s

s1 = Student(78, 96)
print(s1.sum(3, 4))


# Method Overriding
class A:

    def show(self):
        print("In A show")

class B(A):
    
    def show(self): # This method overrides the earlier method of the super class
        print("In B show")

a1 = B()
a1.show()