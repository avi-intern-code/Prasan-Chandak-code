class Computer:
    # Attributes -> Variables
    # Behaviour -> Methods(Functions)

    def __init__(self, cpu, ram): # normally used to initialize variables. Will be called automatically
        self.cpu = cpu # This value will be assigned to the various objects through arguments
        self.ram = ram
    
    def config(self):
        print("Config is: ", self.cpu, self.ram) # cpu and ram will be local variables without self.

com1 = Computer('i5', 16) # This will call __init__() method
com2 = Computer('Ryzen 3', 8)

com1.config() 
com2.config()

