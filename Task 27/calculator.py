# functions to make a calculator

def add(a, b): # function to add two numbers
    return a + b

def subtract(a, b): # function to subtract 2 numbers 
    return a - b

def multiply(a, b): # function to multiply two numbers
    return a * b

def divide(a, b): #funtion to divide two numnbers and except if divided by Zero
    try:
        return a / b
    except ZeroDivisionError:
        return "Division byt zero\n"
# creat file to be able to write to if

while True:
    # asks user to enter two numbers and their name 
    while True:
        try:
            a = float(input("Please enter a first number:"))
            b = float(input("Please enter a second number:"))
            break
        except :
            print ("This is not a number.")

    calculate = input("Please choose: + , - , * , / \n")

    # write the information to the text file

    # if else statement to print the answers
    if calculate in ("+","-","*","/"):
        result = 0
        if calculate == "+":
            result = add(a, b)

        elif calculate == "-":
            result = subtract(a, b)

        elif calculate == "*":
            result = multiply(a, b)

        elif calculate == "/":
            result = divide(a, b)
        output = f"{str(a)} {calculate} {str(b)} = {result} \n"
        print(output)
        with open("output.txt", "a") as file:
            file.write(output)

        user = input ("Continue - y / no - n\n")
        if user == "n":
            break
    
    else:
        print("Invalid input")



# Part 2 of task
user_file = input("Please enter a file name:")
try:
    file2 = open(user_file, "r")
    print(file2.read())
    file2.close()
except IOError:
    print("File does not exist")