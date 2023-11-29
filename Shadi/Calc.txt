def calculate_result(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# Take input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Calculate the result using the calculate_result function
result = calculate_result(num1, operator, num2)

# Print the result for the user
print("Result:", result)