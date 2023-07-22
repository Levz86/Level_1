#creat a program to calculate the numbers
number = 0 # variables to use 
count = 0
total = 0
while number != -1: # while the number entered is not equal to -1
    number = int(input("Please enter a number (-1 to stop)")) # the statement will keep asking to enter a number until -1 is entered
    
    if number != -1: # along with the numbers entered and not being equal to -1 the program will calculate the sum of the number 
         total = total + number #the total with be total + the number entered by the user
         count = count + 1
print (" The average is:" , total/count) #the total divided by the count will give you the average
   
