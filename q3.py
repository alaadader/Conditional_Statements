

#question2
numbers = []
number1 = int(input(f"Enter number 1: "))

number2 = int(input(f"Enter number 2: "))

number3 = int(input(f"Enter number 3: "))

number4 = int(input(f"Enter number 4: "))

number5 = int(input(f"Enter number 5: "))


numbers.append(number1)
numbers.append(number2)
numbers.append(number3)
numbers.append(number4)
numbers.append(number5)

smallest = min(numbers)
largest = max(numbers)

print(f"The smallest number is {smallest}")
print(f"The largest number is {largest}")
