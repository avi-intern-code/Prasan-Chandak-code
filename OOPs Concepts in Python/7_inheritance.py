class A:
    
    def feature1(self):
        print("Feature 1 working")
    
    def feature2(self):
        print("Feature 2 working")

class B(A): # B is inheriting A (single-level)

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B): # Multi-level inheritance
    def feature5(self):
        print("Feature 5 working")

# Multiple inheritance is also supported in python

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()