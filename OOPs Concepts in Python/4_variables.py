class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5 # To modify it we have to use class_name and all objects' variable values will change
#c1.wheels = 7 # will change only for c1 object

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)