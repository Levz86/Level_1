# create a program where the user can choose and calculate the interest or monthly bond payment
import math # calculations will be used
# The user will choose between investment or bond.
print ("investment - to calculate the amount of the interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")
user = input("Enter either ' investment' or 'bond' from the menu above to proceed:") # user to type out either investment of bond
if user.lower() == 'investment': # if user selects investment:
    amount = float(input("What amount of money to you wish to deposit?"))
    interest_rate = float(input("Enter the interest rate(just the number, no%):"))
    term = int(input("Enter the number of years you would like to invest:"))
    interest = str(input("Choose what type of interest 'simple' or 'compound':"))
    print (interest)
    r = interest_rate/100 #calculation for interest rate in %
    if interest.lower() == 'simple': # user to select which type of interest they would like, typing out simple or compound
        a = amount* (1 + r * term) # simple interest to be calculated
        print("The amount of interest you will earn with simple interest is:", a)
    if interest.lower() == 'compound': #compound interest to be calculated
        a = amount* math.pow((1 + r),term)
        print ("The amount of interest you will earn with compound interest is:", a)
elif user.lower() == 'bond': # if user selects bond
    value = float(input("Enter the present value of the house:")) 
    int_rate = float(input("Enter the interest rate:"))
    months = int(input("Enter the number of months to repay the bond:"))
    repayment = ((int_rate) * value)/(1 - (1 + int_rate)**(-months)) # calculation to work out the bond repayments
    print ("The bond repayments will be", repayment)
else:
    print ("You have not enetered anything.") # if the user doesnt select investment of bond. 

   
