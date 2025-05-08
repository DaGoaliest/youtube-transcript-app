# Begin by outlining your code in pseudocode or plain English:

# Prompt the user for two numbers.
n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")

# Check if both inputs are numeric.
try:
    n1 = float(n1)
    n2 = float(n2)
except ValueError:
    print("Both inputs must be numeric.")
    exit()

# Prompt the user to specify an operation.
ops = ["add", "subtract", "multiply", "divide"]
op = input(f"Enter the operation ({', '.join(ops)}): ")

# Based on the operation:
# Perform addition if the user says "add".
if op == "add":
    print(n1 + n2)
elif op == "subtract":
    print(n1 - n2)
elif op == "multiply":
    print(n1 * n2)
elif op == "divide":
    if n2 != 0:
        print(n1 / n2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
