temperature = int(input("Temperature:")) #request user to enter the temperature
if (temperature > 20): #if the temperature is greater that 20 
    print("The user should wear a short sleeved shirt")
else:
    print("The user should wear a long sleeved shirt") #if the temperature is less than 20

weekend = input("is it a weekend (yes/no):") #request user to to state if it is ther weekend or not
if (weekend == "yes"):
    print ("The user should wear shorts") #if yes
else:
    print ("The user should wear jeans") #if no 

sunny = input("is it sunny (yes/no):") # request user to enter yes or no if the sun is shining
if (sunny == "yes"):
    print ("The user should wear a cap") # if yes
else:
    print ("The user should wear a raincoat") # if no
