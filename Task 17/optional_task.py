#creat a program that will read the number of characters, words and lines
file = open("input.txt", "r") # open txt file input.txt
# variables 
characters = 0
words = 0
lines = 0 
# loop for calculating the line, words and characters
for line in file:
    lines = lines + 1
    words = words + len(line.split()) # splits the length of line into words
    characters = characters + len(line.strip()) # strips the length of line into single characters/letters
# prints each one
print("Character:", characters)
print("Words:", words)
print("Lines:", lines)
file.close # close txt file

file = open("input.txt", "r") # open txt file input.txt
input = file.read() # variable to read the txt
count = 0
vowels = ["a","e","i","o","u","A","E","I","O","U"] # list of vowels
for i in input: # loop for every variable in the input txt
    if i in vowels: # counts the number of vowels in the input txt
        count = count + 1 # repeats loo[ untill finish

print ("Vowels:" ,count)

