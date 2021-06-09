class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    
    def __str__(self):
        return "{} {}".format(self.m1, self.m2)

s1 = Student(50, 99) # These values are processed using the __init__() constructor 
s2 = Student(54, 89)

s3 = s1 + s2 # -> calls Student.__add__(s1, s2) # first parameter is self and the second is other

print(s3.m1, s3.m2)

if s1 > s2: # -> calls Student.__gt__(s1, s2) # LHS parameter is first parameter and the self parameter
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a) # Will print the value of a 
# print(a) calls a.__str__()

print(s1) # Will print the address of s1
# print(s1) by default calls s1.__str__() prints module name module class and address

print(s2)