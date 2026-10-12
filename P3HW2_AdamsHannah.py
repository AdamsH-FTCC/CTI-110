# Hannah Adams
# October, 12, 2026
#P3HW1
# Calculates work time and pay for employees


#Outputs needed: Employee name, Pay rate, Hours worked, Overtime hours, Overtime pay, Pay for regular hours, Gross pay

#Determine whether overtime was worked (hours > 40)
#Use if/else logic (required) to calculate overtime pay
#Overtime pay rate is 1.5 × regular pay rate
#Calculate regular pay for regular hours
#Calculate gross pay (total pay)


#Prompt for Employee info
name = input("Enter Employee name: ")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly pay rate: "))

#Check for Overtime & apply overpay
if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    regular_pay = 40 *rate
    gross_pay = regular_pay + overtime_pay
else:
    regular_pay = hours * rate
    overtime_pay = 0
    gross_pay = hours * rate

# Results

print ("-------------------------------------")
print ("Employee Name:", name)
print (f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<20}{"Regular Pay":<15}{"Gross Pay":<10}')
print ("--------------------------------------------------------------------------")
print (f'{hours:<15}{rate:<12}{overtime_pay:<20}{regular_pay:<15}{gross_pay:<10}')