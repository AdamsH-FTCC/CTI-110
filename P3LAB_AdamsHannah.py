# Hannah Adams
# October, 12, 2026
#P3HW1
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money

#get money as a user input
change = float(input("Enter the amount of money: $"))
print (f"Change Amount: {change}")

#Conver value to intiger
change = round(change * 100)
print (f"Change in Cents: {change}")

#determine coins needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print("1 dollar")
    else:
        print(f"{num_dollars} dollars")
else:
    print("No dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print("1 quarter")
    else:
        print(f"{num_quarters} quarters")
else:
    print("No quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print("1 dime")
    else:
        print(f"{num_dimes} dimes")
else:
    print("No dimes")

if num_nickles > 0:
    if num_nickles == 1:
        print("1 nickel")
    else:
        print(f"{num_nickles} nickels")
else:
    print("No nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print("1 penny")
    else:
        print(f"{num_pennies} pennies")
else:
    print("No pennies")