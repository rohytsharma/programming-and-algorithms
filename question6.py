num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter any operator (+, -, *, /): ")

if operator == "+":
    print(f"The result is: {num1 + num2}")
elif operator == "-":
    print(f"The result is: {num1 - num2}")
elif operator == "*":
    print(f"The result is: {num1 * num2}")
elif operator == "/":

    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please use one of +, -, *, or /.")