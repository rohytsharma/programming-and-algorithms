marks = float(input("Enter your marks: "))
if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
elif marks < 70:
    grade = "Fail"
else:
    grade= "invalid"
    print("Invalid marks! Please enter marks between 0 and 100.")

print(f"Your grade is: {grade}")