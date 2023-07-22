
# create a while loop to display count down from 20 - 0
# variable is count = 20
count = 20
# count is more than 0, prints count in descending order because of -1
while count > 0:
    print (count)
    count = count - 1
#creating a loop that will display all the even numbers between 1 and 20
# for even number the range will be the 0 (where it starts), 20 (where is ends) and 2 (the intervals it will jump)
for even_number in range(0, 20, 2): 
     print (even_number, "", end= "") 

print("\n new \n*") #prints the new program and a *
stars = "*" #variable called star
for i in range(0, 5): # for 6 stars to print we select 5 as the end range
    stars = stars + "*" 
    print (stars)

first = int(input("Enter first number:")) # ask user to enter a number
second = int(input("Enter second number:")) # ask user to enter another number
a = 1
while a <= first and a <= second: # a will be less than and equals to the first and second numbers
    if first %a == 0 and second %a ==0: # first and second number is divisable by a(1) with no remainder
        gcd =a # so your gcd will equal a
    a = a + 1 # repeats the loop until the it reaches the first and second numbers entered

print ("The GCD of ", first, "and", second, "is", gcd) # prints the statement





   