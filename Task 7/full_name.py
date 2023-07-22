#create a programme that check if a user has enters their full name

name = input("Please enter your name:") # request user to enter their name
surname = input("Please enter your surname:") # request user to enter their surname
full_name = (f"{name}, {surname}")
if (name != ''):  # if name is not equal to blank
    print(name) # print name
else:
    print ("You haven't entered anything. Please enter your full name.") #or this comment will appear

if len(full_name) <= 4: # if name is less than /equal to 4 the below comment will appear
    print ("You have entered less than 4 characters. Please make sure you have entered your name and surname")
elif len(full_name) > 25: # if the name is more than 25 the below will appear
    print ("You have entered more than 25 characters. Please make sure that you only entered your full name.")
else : 
    print("Thank you for entering your name.")
