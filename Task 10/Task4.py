
digit = int(input("Please enter a number:")) #ask user to enter and digit
print (digit) #prints digit
if (digit%2) ==0 and (digit%5)==0 : # both conditions must be = to 0
    print ("The number is divisible by 2 and 5") # then the program will print this statement
if (digit%2) ==0 or (digit%5)==0 : # the number the user entered is divisible by either 2 or 5 not both
    print ("The number is divisible by 2 or 5")
else: # if the number is not divisible by any them print else
   print ("The number", digit, "is not divisible by 2 or 5")
   