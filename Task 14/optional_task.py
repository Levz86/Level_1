car= input("Please enter your faourite car:") # compilation error,  the varible name does not match the variables in the print statements. will not follow through
gears = (input("how many gears does this car have?")) # runtime error, the input for gear is not recognised as an integer. the program will pick it up as a string
while gears > 7:
    print ("cars only have 6 gears please enter a valid number:")
    gears = int(input("how many gears does this car have?"))
if gears == 6:
    print ("The", car, "is a fast car!")
else:
    print "The", car, "is a slow car." # compilation error, there are no parenthsis in the print statement. hence it will now print

print ("\n")
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
solve = (a + b + c / 3) # logic error a+b+c should be in parenthesis before dividing /3. else it will take c and divide by 3
print ("The average is", solve)
       
