# Hannah Adams
# October, 12, 2026
#P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

print ("Lets calculate your grades!")

mod_1 = int(input("Enter grade for Module 1: "))
mod_2 = int(input("Enter grade for Module 2: "))
mod_3 = int(input("Enter grade for Module 3: "))
mod_4 = int(input("Enter grade for Module 4: "))
mod_5 = int(input("Enter grade for Module 5: "))
mod_6 = int(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Sum of grades: {sum}")
print(f"Average grade: {avg}")

if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

# TO DO: finish this





