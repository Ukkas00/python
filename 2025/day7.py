while True:
    # Check whether the input is number or not before converting to int or float (Note: If user has provided number convert it to int or float if not then ask for number again)
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    check_num1 = num1.isdigit() 
    check_num2 = num2.isdigit()

    if check_num1 and check_num2:
        num1 = float (num1)
        num2 = float (num2)
        break
    else:
        print("numbers are only allowed")
    
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
 


