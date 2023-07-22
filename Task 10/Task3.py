swimming = float(input("Please enter your time it took to complete swimming:")) #ask user to enter the time to complete swim 
print ("The time to complete swimming is:", swimming)
cycling = float(input("Please enter your time it took to complete cycling:")) #ask user to enter the time to complete cycle
print ("The time to complete swimming is:", cycling)
running = float(input("Please enter your time it took to complete running:")) #ask user to enter the time to complete run
print ("The time to complete swimming is:", running)
time_to_complete = (swimming + cycling + running) # add the 3 times to get total time to finish triathlon
print ("The total time to complete the triathlon:", time_to_complete)

if (time_to_complete < 100): # if the time to complete is less than 100 
    print ("Provincial Colours") # they receive this award
elif (time_to_complete >= 100 and time_to_complete <= 105): # if the users time to complete is between 100 and 5 min later
    print ("Provincial Half Colours") # they receive this award
elif (time_to_complete >= 100 and time_to_complete <= 110): # if the time to complete is between 100 and 10 min later
    print ("Provincial Scroll") # they receive this award
if (time_to_complete > 110): # it the time to complete is after 100 + 10
    print ("No award")  # the user gets no award





