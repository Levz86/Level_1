
#defining an Adult class with methods
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colout = eye_colour

    def can_drive(self): #can drive method if the user is older than 18
        print(f"{self.name} is old enough to drive.")
        

#defining a child class that inherits from the adult class and overrides the can drive method.
class Child(Adult):
       def can_drive(self):
            print(f"{self.name} is too young to drive.")

# request input from user about name, age, hair and eye colour

name = input("What is your name?")
age = int(input("What is your age?"))
hair_colour = input("What is your hair colour?")
eye_colour = input("What is your eye colour?")

# call the can drive method of the person
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

person.can_drive()