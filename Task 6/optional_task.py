side1 = int(input("Enter first side : ")) # request user to enter 3 sides of triangle
side2 = int(input("Enter second side : "))
side3 = int(input("Enter third side : "))
s = (side1 + side2 + side3)/2 
print (s)
area =  (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5 
print ("The area of the triangle is%0.2f " %area)