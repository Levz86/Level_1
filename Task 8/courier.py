price = float(input("Please enter the price of the item to purchase:\n")) # request user to enter price of item to purchase
distance = float(input("Please enter the total distance for delivery:(km.)\n")) # request user to enter the distance for delivery
freight_or_air = int(input("choose \n1.Air or \n2. Freight")) #choos a mode of transport
print(freight_or_air)
cost_per_distance = 0 #if no option is chosen
if (freight_or_air == 1): #to choos air
    cost_per_distance = 0.36
if (freight_or_air ==2): # to choose freight
    cost_per_distance = 0.25

insurance = int(input("choose \n1. Full insurance or \n2. Limited insurance:"))
print (insurance) # ask user to choose the type of insurance 
cost_of_insurance =  0 #if no option is chosen
if (insurance ==1):
    cost_of_insurance = 50.00 # to choos full
if (insurance ==2):
    cost_of_insurance = 25.00 # to choose limited

gift = int(input("gift: \n1. Yes \n2.No"))
print (gift) # request user to yes or now if its a gift

delivery = int(input(" choose a delivery: \n1. Priority \n2. Standard"))
print (delivery) # choose delivery
cost_of_delivery = 0 # if no option is choose
if (delivery ==1): # for priority
    cost_of_delivery = 100
if (delivery ==2): # for standard
    cost_of_delivery = 20

total_cost = price + distance*cost_per_distance + insurance + gift + delivery
print ("total_cost: ", total_cost)



