import math
#ask user to enter the below inputs 
nights = int(input("Nights you would like to stay: \n"))
city = input("Which city are you flying to (India , Austrailia , London):\n")
days = int(input("How many days do you need a car for:"))
# add function 1 for the hotel cost nights needed * cost
def hotel_cost(nights):
    return nights * 1200
# function 2, the user chooses one off the options
def plane_cost(city):
    if city == "India":
        return 8000
    elif city == "Austrailia":
        return 15000
    elif city == "London":
        return 12000
# function 3 number of days for car rental * cost
def car_rental(days):
    return days * 500
# function 4 to calculate everything             
def holiday_cost(nights , city, days):
    hotel = hotel_cost(nights)
    print ("The total cost for the hotel will be:", hotel)
    plane = plane_cost(city)
    print ("There cost of the flight will be:", plane)    
    car = car_rental(days)
    print("The cost for the car rental for", days,"days is:R",car)
    total = hotel + plane + car
    print("The total cost is R", total)
holiday_cost(nights,city,days)             

