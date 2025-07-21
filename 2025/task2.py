# Task (Calculator)
# Ask the user for two numbers
# Ask the user for which operators to use (+,-,/,*)
# Accoring to the operator user provides perform the operation with two numbers and print the value

num1=float(input("enter the first number"))#cheak whether the input is a number or not before converting to int or float(note: if user has provided number convert it to int or float if not then ask user to enter a valid number)
num2=float(input("enter the second number"))

operator = input("Enter the operator (+, -, *, /): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Invalid operator")                