phrase = "Good Morning Sunshine!"
space = ""

for i in range(len(phrase)):
    if i % 2 == 1:
        space += phrase[i]. upper()
    else:
        space += phrase[i]. lower()
print (space)
print ("\n")
new_phrase = phrase.split()
for i in range(len(new_phrase)):
    if i % 2 ==0:
        space += new_phrase[i].upper()
    else:
        space += new_phrase[i].lower()
done = "".join(space)
print (done)




