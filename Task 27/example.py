while True:
    try:
        x = int(input("enter a number:"))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
