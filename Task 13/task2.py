# creat a prog that work out which years are leap and whic are now from the year and time frame the user enters
year = int(input("What year do you want to start with?")) # asks user to enter the year to start with
number_of_years = int(input("How many years do you want to check?")) # asks user how many years to check to see which are leap and are not
for number_of_years in range (1, number_of_years): # number of year range from 1 to what the user enters
    if year % 4 != 0 : # if the year is not divisable by 4 it will not equal 0
        print(f"{year} is not a leap year.") # and therefore this statment will print, 
        year = year + 1
    else :
        print(f"{year} is a leap year.")# else it will print the even years
        year = year + 1
