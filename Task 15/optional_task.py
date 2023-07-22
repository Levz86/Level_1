# to create and check if a strint is a palindrome
# ask user to enter a string and if the string is equal to the string in reverse
# it is a palindrome, if not = to -1 the is not a palindrome. [start: stop: step] the start and stop is empty -1 will be reverse
string = input("Please enter a string:")
if string == string[::-1]:
    print ("This string is palindrome.")
else:
    print ("This string is not a palindrome.")

