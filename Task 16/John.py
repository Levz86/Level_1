a = "" #variable a #
#an empty list []
list = []
#loop to see that name is not equal to john will carry on asking for a name until John is entered 
while a != "John":
    a = input("Please enter a name:")
    list.append(a) #append allows addition of names
print ("ïncorrect names:" , list)
