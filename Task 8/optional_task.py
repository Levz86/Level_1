employee = int(input("Are you a \n1. Manager  \n2. Salesperson")) #ask user to enter their employee status
# declare variables for sales person
gross_sales = 0.0
commission = 0.0
fixed_salary = 2000.0
# declare variables for manager
hour_work = 0.0
hour_rate = 40.0
total_wage = 0.0
if (employee == 2): # if the users selects 1 (salesperson)
    gross_sales = int(input("What is the gross sales for the month?"))
    commission = gross_sales * (8/100)
    total_wage = commission + fixed_salary
    print ("R",total_wage)
# or if he selects 1 for the manager
else:
    hour_work = int(input("Enter the number of hours worked for the month:"))
    total_hours = (hour_work*40)
    print("R",total_hours)

print ("Total wages for the Salesperson:", total_wage) 
print ("Total wages for the Manager:", total_hours)

