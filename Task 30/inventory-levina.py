#from tabulate import tabulate
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        pass
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]
        pass
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data(): # function for reading the file inventory.txt
   #try_catch block
    try:
        # file variable to read .txt file
        file = open("inventory.txt", "r")
        info = next(file).strip().split(",")
        #loop for writing data in dictionary after extracting length wise
        for line_of_text in file:
            shoe_list.append(dict(zip(info, line_of_text.strip().split(",") )))
    #except block        
    except FileNotFoundError:
        print("File inventory.txt no available")        

    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    #try cathc block
    try:
        #ask user to enter all the relevent info regarding the product
        new_country = input("Please enter the country:")
        new_code = input("Please enter the code:")
        new_product = input("Please enter the product new:")
        new_cost = int(input("Please enter the cost(numbers only):"))
        new_quantity = int(input("Please enter the quantity:"))
        #adds items to the list 
        new_shoe = Shoe(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_list.append(new_shoe)
        #opens file and write the info to the file
        file = open("inventory.txt", "a+")

        file.write(f"\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}")
        print("\n Thank you, your product has been loaded!\n")

        file.close()

    except FileNotFoundError:
        print("\nSorry, this file does not exist!\n")

    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    #veiw all the items in the inventory list
    head = ["Country", "Code", "Product", "Cost", "Quantity"]
    shoe_data_list = []
    for shoe in shoe_list:
        shoe_data_list.append(shoe.__str__())
    print("\n\nHere are all your stock details: ")
    print(shoe_data_list)# headers=head, tablefmt="grid")#Tabulate not working


    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():

    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:

    shoe_list.clear()
    read_shoes_data()

    try:
        menu = int(input("""\n 
        Please choose one of the following options:
    1 => To view all your stock details
    2 => To capture data about an item and add this to your stock list
    3 => To view the total value of each item in your stock
    4 => To view items low on stock and re-stock 
    5 => To search an item by the product code
    6 => To view items that are on sale (highest stock products) 
    0 => To exit the system
        """))
        if menu == 1:
            view_all()
        elif menu == 2:
            search_shoe()
        elif menu == 3:
            value_per_item()
        elif menu == 4:
            re_stock()
        elif menu == 5:
            highest_qty()
        elif menu == 6:
            capture_shoes()
        elif menu == 0:
            print("Thank you")
            exit()
        else:
            print("\n Wrong choice, please try again!")

    except ValueError:
        print("\n Please ensure you enter a number from 0 to 6!")
