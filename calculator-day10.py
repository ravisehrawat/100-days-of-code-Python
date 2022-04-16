from calculator_art import logo
print(logo)

#addition
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1, n2):
    return n1 * n2

#division
def divide(n1, n2):
    return n1 / n2

operations = { "+": add, 
                        "-": subtract, 
                        "*": multiply, 
                        "/": divide }
     

print("Welcome to the calculator!")
def calculator():
    Calculation = True
    num1 = float(input("Enter a number: "))       #input first number
    while Calculation:
        num2 = float(input("Enter next number: "))    #input second number

        for operation in operations:
            print(operation)

        operator = input("Enter operator: ")           #input operator
        if operator in operations:
            print(f"{num1} {operator} {num2} = {operations[operator](num1, num2)}")
            num1 = operations[operator](num1, num2)
        else:
            print("Invalid operator")
        cont = input("Want to Continue with answer? (y/n): ")
        if cont != "y":
            Calculation = False
            print("Thank you for using the calculator!")

Calculation = True
while Calculation:
    calculator()
    cont = input("Want to Continue with new number? (y/n): ")
    if cont != "y":
            Calculation = False
            print("Goodbye! Have a nice day!")
