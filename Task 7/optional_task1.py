#Programm to test whether a number is odd or even
number = int(input("Please enter any integer odd or even:")) # ask user to enter an integer
if (number %2) == 0: # the number the user entered divided by 2, with no remainder i.e 0 it is even  
    print ("The number is even")
# if there is remainder it will be odd.
else: 
    print ("the number is odd")