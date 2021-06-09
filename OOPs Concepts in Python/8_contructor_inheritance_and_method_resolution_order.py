# Constructor inheritance and Method Resolution Order (MRO)

class A:

    def __init__(self):
        print("In A init")
    
    def feature1(self):
        print("Feature 1 working")
    
    def feature2(self):
        print("Feature 2 working")

# sub class can access all the features of super class but 
# super class cannot access any features of sub class

class B(A): # B is inheriting A (single-level) 

    # If init is not defined in B, it will call the init of A
    def __init__(self):
        super().__init__() # Super allows access to the super class super represents super class
        # This will call the constructor of class A
        print("In B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# a1 = B() # Object of B class will still call the constructor __init__() of A class

class C:

    def __init__(self):
        print("In C init")
    
    def feature1(self): # method with same name as in class A which D is inheriting alongside C 
        # To test which one is inherited, we change the output
        print("Feature 1-C working")
    
    def feature6(self):
        print("Feature 6 working")

class D(A, C): # Multiple inheritance

    def __init__(self):
        super().__init__() # Method Resolution Order goes from left to right
        # This will call the constructor of left class i.e. A
        print("In D init")

    def feat(self):
        super().feature2()

a1 = D()
a1.feature1() # This will call the method feature1() of class A 
a1.feat()