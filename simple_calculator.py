# Take user input
nr1 = float(input("Enter the first number: "))
nr2 = float(input("Enter the second number: "))
num_operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if num_operator == "+":
    result = nr1 + nr2
elif num_operator == "-":
    result = nr1 - nr2
elif num_operator == "*":
    result = nr1 * nr2
elif num_operator == "/":
    result = nr1 / nr2
else:
    print("Invalid operation")

# Print result
print("Result: ", result)