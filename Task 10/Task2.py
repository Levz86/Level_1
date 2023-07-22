# creats a program that calculates the area of a shape
shape = int(input("Please enter the shape of the building: \n1. Square \n2. Rectangular \n3. Round"))
print (shape) # ask the user to select a shape
square = 0 # declares variable
if (shape == 1): # if user selects square (no1)
    side = float(input("Enter side of square")) # reauest user to enter a measurement for the square)
    square_area = (side*side) # calculates the area of the square
    print ("the area of a square is:", square_area) # prints the area
elif (shape == 2): # if the user selects rectangle
    length = float(input("Enter the length of the retangle")) 
    width = float(input("Enter the width of the rectangle"))
    rectangle_area = (length * width)
    print ("The area of the rectangle is", rectangle_area)
else: # if the user selects no3
    pi = float(3.14)
    radius = float(input("Enter the radius of the circle"))
    circle_area = (pi * (radius**2))
    print ("The area of the circle is", circle_area)
