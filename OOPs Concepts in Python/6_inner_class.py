class Student: # Outer Class

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop() # lap is an object of the Laptop class 
        # Object of inner class creater inside the outer class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show() # Calls the lap object method show()

    class Laptop: # Inner Class

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8
        
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("A", 2)
s2 = Student("B", 3)

s1.show()
print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

lap3 = Student.Laptop() # Object of inner class creater outside the outer class