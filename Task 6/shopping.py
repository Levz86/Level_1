product1 = input("Please enter a product name:") # ask user to enter 3 products
product2 = input("Please enter a second product name:")
product3 = input("Please enter a third product:")
price1 = float(input("product1 price")) # ask user to enter the prices for each
price2 = float(input("product2 price"))
price3 = float(input("product3 price"))
addition = (price1 + price2 + price3) # additiong for the 3 products
print (addition)
average = round(addition,2) #average of the 3 products
print (average)
print ("The total of product1,product2,product3 is" + "R"(addition) "and the average price of the items are R" + (average))