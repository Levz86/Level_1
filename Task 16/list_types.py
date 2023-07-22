# stores 3 names in a list of strings and create the variable "friends_names"
# .extend allows to add multiple names to a list
friends_names = []
friends_names.extend(["Suneel", "Darshana", "Aradhya"])
print(friends_names)

# to print the first name
print(friends_names[0])

#to print the last name
print(friends_names[-1])

# to print the length of the list
i=0
for friend in friends_names:
   i=i+1
print("The length is", i)
# friends ages in a list. and prints each name with the age next to it
friends_ages = [37, 25, 18]
print (friends_names[0] + " 37")
print (friends_names [1] + " 25")
print (friends_names[2] + " 18")

