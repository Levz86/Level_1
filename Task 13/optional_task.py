# ask user to enter a number and cast it to an integer 
user = int(input("Please enter a number:"))
num = user # variable for users number
for i in range(0, num): # varible i will range from 0 to the number the user entered
    if num > 10: # if the number is greater than 10, the number will be printed out as many times as its value
        print (num)
        i = i + 1 # will repeat the loop until the users number is reached
    else: # if the users number is smaller than 10 it will print too small
        print ("Sorry,too small")
        break # stops the loop
