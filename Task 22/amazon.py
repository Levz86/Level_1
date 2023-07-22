# Funcition import
import statistics

# File opening
with open( 'input.txt' ) as textfile :
    # Reading the file
    textRead = textfile.read()
#Opening and writing to the output file "out.txt" 
text_files = open("output.txt", "x")
text_files = open("output.txt", "w")
#Looping thru each line of the file
for line in textRead.split('\n'):
    mini, operations, numbers = line.split(':')
    operations = operations.strip() 
    mini = mini.strip() 
    numbers = map(float, numbers.strip().split(",") )


    if operations == 'avg' :
        text_files.write('\nThe value of average of [1,2,3,4,5,6] is '+str(statistics.mean(numbers)))

    if operations == 'min' :
        text_files.write('\nThe value of min of [1,2,3,4,5,6] is '+str(min(numbers)))

    if operations == 'max' :
        text_files.write('\nThe value of max of [1,2,3,4,5,6] is '+str(max(numbers))) 


text_files.close()
text_files = open("output.txt", "r")
print(text_files.read())
