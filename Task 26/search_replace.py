def search_replace():
    #ask the user to enter a string
    string = input("Please enter a string:")
    #if the user input is not 0
    if string != 0 :
        #substring - ask user to enter
        sub_string = input("Please enter a substring:")
        #ask user to enter a new string to replace
        replace_string = input("Please enter a string to replace the substring:")

        new_string = string.replace(sub_string,replace_string)
        print("The new new string is:" , new_string)
        search_replace()
        print()
search_replace()