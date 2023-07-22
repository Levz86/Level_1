
menu = ["coffee","muffin","smoothie","hotchocolate"]
stock = {"coffee" : 5,
         "muffin" : 12,
         "smoothie" : 7,
         "hotchocolate" : 10}
price = {"coffee" : 15,
         "muffin" : 25,
         "smoothie" : 50,
         "hotchocolate" : 30}
total = 0
for item in menu:
    quantity = stock[item]
    cost = price[item]
    total = total + quantity * cost
print ("Total stock: R",total)