print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")