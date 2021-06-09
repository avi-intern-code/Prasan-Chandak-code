class Computer:
    #pass # id(c1) will give an error if the class is empty
    def __init__(self):
        self.name = "x"
        self.age = 54
         
    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else: 
            return False

c1 = Computer() # will call __init__() method
c1.age = 30
c2 = Computer()

if c1.compare(c2): # Here c1 becomes self and c2 refers to next argument (other)
    print("They are same")
else:
    print("They are different")

# print(id(c1)) # Will print the address of c1
# print(id(c2))