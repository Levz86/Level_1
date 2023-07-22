# asks user to enter something that will count all the letters
word = input("Please enter something:")
my_dict = {} # variable
for i in word: #  for loop to iterate through
    if i in my_dict: # if startement to check i is in frequency
        my_dict[i] = my_dict[i] + 1 # increment the frequency
    else:
        my_dict[i] = 1 # assign 1 to frequency
print (my_dict) #print output

