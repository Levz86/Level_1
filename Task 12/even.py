#creat a program that will print out the even numbers
user_number = int(input("Please enter a number:")) # asks the user to enter a number
count = 2 # varible to count in 2's (not equal to 0)
while count <= user_number: #count will be less than but also equal to the number the user enters
    print (count) #print count but below count will jump in intervals of 2
    count = count+2