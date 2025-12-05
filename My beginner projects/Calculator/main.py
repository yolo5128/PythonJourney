
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /, **): ")

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == "**":
    result = num1 ** num2
    print(f"The result of {num1} ** {num2} is {result:.2f}")