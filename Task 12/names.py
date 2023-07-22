count = 0 #variable for count to be 0
name = 0 #variable for name to be 0
while name != "stop": # if name is not equal to stop the following will run
    name = input("Please enter all the pupils names type stop when done:") # asks user to enter a pupils name and type stop when done   
    if name == "stop": #if the user types stop the program will stop asking the above
        print (f"Total number of pupils entered:{count}") #and it will print the following sentence
        break
    count = count + 1 # when the user types stop it will count the number of pupils
    