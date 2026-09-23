# Hannah Adams
# September, 9, 2026
# P1 HW2
# Working with integers again to calculate expenses for a trip

# A whimsical intro because I've been into adventure anime again. Actually this whole thing is gonna sound fantasy-esque.
print ("Hello there, adventurer! It seems you need help planning for your next quest.")
print()

#Ask user their budget
startB = int(input("Lets see... how much have you put aside for your journey?: "))

#Ask user their travel destination
destination = input("A reasonable amount, now where would you like to go?: ")

#Ask user for amount they will spend on gas
gas = int(input("How much will be spent on fuel for your steed?: "))

#Ask user for amount they will spend on shelter
accommodation = int(input("What have you in mind for lodgings?: "))

#Ask user for amount they will spend on food
food = int(input("How much will be spent on rations?: "))

#Add expenses together then subtract expenses from budget
all_expenses = gas + accommodation + food
leftovers = startB - all_expenses

#Display results
print("According to my orb, you'll be spending:", all_expenses ,"$")
print("And that will leave you with:", leftovers, "$ for your adventure to", destination, "!")