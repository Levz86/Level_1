#=====importing libraries===========
'''This is the section where you will import libraries '''

#====Login Section====

'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#variables
user_details = [] # empty list
current_user = ""
number_tasks = 0
number_users = 0

# user enters user name and password. if it not admin and adm1n, the user user will be prompted to enter is again until admin is entered
username = input("Please enter your username:")
password = input("Please enter your password:")
#if username != "admin":
print ("You are not an admin user, only admin can register new users.")
username = input("Please enter your username:")
password = input("Please enter your password:")

#else:      
#opens the user.txt file and reads it
with open("user.txt", "r+") as file:
    for lines in file: # temp variable lines 
        temp = lines.strip() # another temp variable to strip the lines in user.txt
        user_details.append (temp) #user_details/empty list will the add(append) the lines in user.txt ie the username and password
# opens the boolean loop. true meaing the loop will run indefinitely
    while True:   
        input_details = f"{username}, {password}" # variable to check for both username and password
        if input_details in user_details:
            current_user = username
            break
        else:
            print ("Wrong username and password. Please try again:")
            break
    file.close ()
while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # 'ds' added for task 2 as an option to select
    menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds - Display Statistics 
        e - Exit
        : ''').lower()
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if menu == 'r': # if the user selects r the program will registera new user. username and password will be added. and confirmation password
        if username == "admin":
            new_username = input("Please enter your new username:")
            new_password = input("Please enter your new password:")
            confirm_password = input("Please confirm your new password:")
            if new_password == confirm_password: #checking that the password matches
                with open("user.txt", "a") as f:
                    f.write(f"\n{new_username}, {new_password}") # format to entered username and password to user.txt
                    print ("New user registered")
                    break
            while new_password != confirm_password:
                print("The password doesnt not match Please try again:")
                confirm_password = input("Please confirm your new password:") # will keep asking until the correct confirmed password is entered
                with open("user.txt", "a") as f:
                    f.write(f"\n{new_username}, {new_password}") # format to entered username and password to user.txt
                    print ("New user registered")
                    break
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a': # if the user selects a, the program will add a task, asking the user to enter all info regarding the task
        user = input("Please enter your username who this task is for?")
        task = input("Please enter the title of the task:")
        des_task = input("Please enter a short description of the task:")
        due_date = input("Please enter a due date:")
        current_date = input("Please enter todays date")
        task_completed = "No"
        #to open the txt and then add the task in the txt file
        with open("tasks.txt", "a") as add:
            add.write(f"\n{user}, {task}, {des_task}, {due_date}, {current_date}, {task_completed}") # format 
            print ("The new task has been saved")
               
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va': # if the user selects va this will allow the user to view all tasks
        files = open("tasks.txt", "r")
        for line in files: # opens file and strips and splits the tasks
            tempa = line.strip()
            tempa = tempa.split(", ")
                                               
            print ("User:", tempa[0])
            print ("Task:", tempa[1])
            print ("Description:", tempa[2])
            print ("Due date:", tempa[3])
            print ("Current date:", tempa[4])
            print ("Task completed:", tempa[5])
        files.close()
                  

        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm': # if the user selects vm this will allow the user to view all their tasks
        files = open("tasks.txt", "r")
        lines = files.readlines() # reads all the tasks 
        for line in lines:
             tempa = line.strip()
             tempa = tempa. split(", ")
       
        print ("User", tempa[0])
        print ("Task", tempa[1])
        print ("description", tempa[2])
        print ("due_date", tempa[3])
        print ("current_date", tempa[4])
        print ("Task completed", tempa[5])
        files.close()
            
            
        '''In this block you will put code the that will read the task from task.txt file and
                print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
                You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same print it in the format of Output 2 in the task PDF'''
        # ds added for task 2 to display statistics
        #will calculate the total number of tasks and total number of users in both files
    elif menu == "ds":
        with open("tasks.txt","r") as task_file:
              for line in task_file:
                   number_tasks = number_tasks + 1
        print (f"\nTotal number of tasks:", {number_tasks})
        with open("user.txt","r") as username:
              for line in username:
                   number_users = number_users + 1
        print (f"\nTotal number of users:", {number_users})

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
        