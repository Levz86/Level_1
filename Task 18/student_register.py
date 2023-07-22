#creat a loop that runs for the amount od students registered
#asks user to enter the amoutn of students
#variable count 
students = int(input("How many students are registering?"))
count = 0
register_form = open("reg_form.txt", "a") # opens a txt and a for append as in adds to the txt
# loop for variable numb in range of 0 to the number of students
for num in range(0, students):
    number = input("Please enter your ID number:") # each student to enter an ID number
    register_form.write(number + "...........\n") 
    # Id will be added to a reg_form.txt on a new line for every entry

register_form.close()  

  