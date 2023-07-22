num1 = 10
num2 = 20
num3 = 30
if (num1 < num2):
    print ("Value",num2,"is greater then",num1)

if (num1%2 == 0):
    print ("Value",num1, "is an even number.")
else:
    print ("Value",num1, "is an odd number.")
 
c = min (num1,num2,num3)
a = max (num1,num2,num3)
b = (num1+num2+num3) - c -a
print("value in sorted order: ",a,b,c)
