# Create a program that calculates a persons bmi
weight = float(input("What is your weight in kg?")) #asks user to enter weight in kg
height = float(input("What is your height in m?")) #asks user to enter height in m
bmi = (weight/(height*height)) # equation to calculate bmi
if bmi >= 30:
    print ("You are obese.") # if users bmi is more than 30
elif bmi >=25:
    print ("You are overweight.") # if users bmi is more than 25
elif bmi >= 18.5:
    print ("You are normal.") # if users bmi is more than 18.5
elif bmi <= 18.5:
    print ("You are underweight.") # if users bmi is less than 18.5
