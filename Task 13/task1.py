#create a prog that allows user to enter a number and the prog will print out the time table for that number till 12
user_input = int(input("Please enter a number:")) # asks user to ener a number
y = int(input("Please enter another number:"))
x = user_input # x will be equal to unput user
for y in range(1, 13): # the y will go up to 13 ie 12
    print(f"{x} * {y} = {x*y}") # formuber fo rtimes table
    