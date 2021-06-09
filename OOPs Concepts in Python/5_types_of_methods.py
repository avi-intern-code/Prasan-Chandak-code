
class Student:

    school = 'Telusko' # Static/Class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1 # m1 - argument passed in__init__(); self.m1 - to particular object variable
        self.m2 = m2 # Instance variable 
        self.m3 = m3

    # Instance method
    def avg(self): # Instance method as self is passed as an argument to call it - object_name.avg()
        return (self.m1+self.m2+self.m3)/3

    # Class method
    @classmethod # For creating a class method we have to use decorators
    def getSchool(cls): # working with instance var use 'self'; working with class var use 'cls' keyword
        return cls.school
        
    # Static method
    @staticmethod
    def info(): # 'cls' or 'self' are not used
        print("This is the Student class")
    # This type of method has nothing to do with class and instance variables


    def get_m1(self):
        return self.m1 # Accessor method - getter

    def set_m1(self, value):
        self.m1 = value # Mutator method - setter

s1 = Student(34, 67, 32)
s2 = Student(34, 45, 67)

print(s1.avg())
print(s2.avg())
#print(s1.info()) # This calls the info() function

print(Student.getSchool()) # Works after using decorator

#s1.info() # This will not work as s1.info() will result in 1 positional argument
Student.info() # Calling static method
