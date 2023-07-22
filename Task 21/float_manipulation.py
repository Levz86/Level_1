import math # as per task instructions
import statistics
list_float= [] #empty list
# for loop to range from 0 to 10
for i in range(0, 10):
    user = float(input("Enter a number:"))# will keep asking to enter a number until 10 are entered
    list_float.append(user) # adding the user number to the list
# listing the numbers 
print(f"The list of numbers : {str(list_float)}")
# calculating the sum of all the numbers
total= sum(list_float)
print(f"The total of all the numbers is: {total}")
#pulls the maximum number amoungst what the user entered 
print(f"The maximum number is : {max(list_float)}")
#pulls the minimum number amoungst what the user entered 
print(f"The minimum number is : {min(list_float)}")
# calculates the average of the 10 numbers
average = total/10
print(f"Average is: {average}")
# calculates the median of the numbers
median = statistics.median(list_float)
print(f"The median is: {median}")

