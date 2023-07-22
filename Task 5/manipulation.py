str_manip = input ("Please enter a sentence:") # ask user to  enter a sentence
print (str_manip)

print (len(str_manip)) #calculates the number of characters

rep_word = str_manip.replace("a" , "@") # replaces all the a 's with @
print (rep_word)

print (str_manip [-1:-4:-1]) # shows the last 3 letters

print (str_manip[:3] + str_manip[-2:]) # 