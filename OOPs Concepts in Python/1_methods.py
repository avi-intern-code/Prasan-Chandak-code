class Computer:
    # Attributes -> Variables
    # Behaviour -> Methods(Functions)
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer() # Constructor
#print(type(com1))
com2 = Computer()

Computer.config(com1) # Calling config() for com1
Computer.config(com2)

com1.config() 
com2.config()

