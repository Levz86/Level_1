# abbreviation dictionary
abbreviations = {"omg" : "oh my god",
                 "tmi" : "to much information",
                 "SA" : "South Africa",
                 "eta" : "estimated time of arrival",
                 "MIB" : "Men in Black"}
# add 2 more abbreviations
abbreviations.update({"bmi" : "Body mass index",
                       "ibs" : "Irritable bowel syndrome"})
print(abbreviations)
# ask user to enter abbreviation
user = input("Please enter abbreviation:")
if user in abbreviations:
    print(abbreviations[user]) # if it is in the dictionary
else:
    print("Abbreviation not found") # if it is not in the dictionary