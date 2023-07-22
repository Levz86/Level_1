#asigning a variable to the text file
numbers1 = "numbers1.txt"
numbers2 = "numbers2.txt"
all_numbers = "all_numbers.txt"
# opens and read the numbers1 text file and makes it "a" variable
num1 = open(numbers1,"r+")
a = num1.read().split()
# opens and read the numbers2 text file and makes it "b" variable
num2 = open(numbers2,"r+")
b = num2.read().split()
# stores write
c = open(all_numbers, "w")
#temp variables
temp1 = 0 
temp2 = 0
#opens and checks both file content and write in ascending order
while temp1 < len(a) and temp2 < len(b):
    data1 = int(a [temp1])
    data2 = int(b [temp2])
    if data1 <= data2:
        c.write(str(data1) + "\n")
        temp1 = temp1 +1

    elif data1 > data2:
        c.write(str(data2) + "\n")
        temp2 = temp2 + 1
# puts the numbers into file all_number.txt
while temp1 < len(a):
    c.write(str(a[temp1]) + "\n")
    temp1 = temp1 + 1

while temp2 < len(b):
    c.write(str(b[temp2]) + "\n")
    temp2 = temp2 + 1

print("Look at all_numbers.txt")
#close all files
num1.close()
num2.close()
c.close()
