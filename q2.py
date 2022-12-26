# first number
num1 = input("Enter the first number: ")
if not num1.isdigit():
  print("Error: Please enter a valid age (only numbers)")
  exit()
num1 = int(num1)

num2 = input("Enter the second number: ")
if not num2.isdigit():
  print("Error: Please enter a valid age (only numbers)")
  exit()
num2 = int(num2)

# Get the operation from the user
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. ^")
print("6. %")
op = input("choose the operation you need from above ")

if op == "1" or op == "+":
    operation="+"
elif op == "2" or op == "-":
    operation="-"
elif op == "3" or op == "*":
    operation="*"
elif op == "4" or op == "/":
    operation="/"
elif op == "5" or op == "^":
    operation="**"
elif op == "6" or op == "%":
    operation="%"
else:
    print("Error: Please enter a valid operation")
    exit()

# Perform
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
elif operation == "**":
  result = num1 ** num2
elif operation == "%":
  result = num1 % num2

# Print the result
print(f"Result: {result}")

# options for the output
print("1. Normal rounding")
print("2. No decimal point")
print("3. Exit")

# output option
output_option = input("Enter the output option: ")

if output_option == "1":
    print(f"Rounded result: {round(result)}")
elif output_option == "2":
    print(f"Result without decimal point: {int(result)}")
elif output_option == "3":
    exit()
else:
    print("Error: Please enter a valid option")

print("Thank you for using the program!")
