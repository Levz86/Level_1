number = 0
while number == 0:
    user = int(input("Enter a number that is less than or equal to 100:"))
    if user <= 100:
        number = 1
    
if number %2 ==  0:
    print ("Output:", user * 2)
else :
    print ("Output:", user * 3)
