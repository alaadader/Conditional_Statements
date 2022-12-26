#Question 1
print("Hi,let's start")
name = input("Please enter your name: ")
if not name.isalpha():
  print("Error: Please enter a valid name (only letters)")
  exit()

age = input("Please enter your age: ")
if not age.isdigit():
  print("Error: Please enter a valid age (only numbers)")
  exit()
age = int(age)

address = input("Please enter your address: ")

print(f"Hello Mr/Ms {name} age {age} located in {address}.\nThanks for being one of our community.\nEnjoy!")
