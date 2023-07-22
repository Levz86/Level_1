#creating a program that will read DOB.txt and open in python
file = open("DOB.txt", "r") # to open the file
lines = file.readlines() #variable lines to read the lines

print ("Names\n") # Title. and then temp variable line for striping and then spliting the txt
for line in lines :
    temp = line.strip() # separetes the characters
    temp = temp.split () # [" "," "," "]
    
    print (" ".join(temp[0:2])) # will join the 1st and 2nd words i.e the name and surname
file.close

file = open("DOB.txt", "r")
dates = file.readlines()
# tital to pull out the birthdates
print ("\nBirthdate\n")
for date in dates :
    day = date.strip()
    day = day.split()

    print(" ".join(day[2:5])) # will join the date, month and year
file.close