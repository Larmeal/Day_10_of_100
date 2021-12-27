# เครื่องคิดเลข

from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 / n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

operator = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply,
    }

again = True
ask = float(input("What's the first number?: "))
print("""+
-
*
/""")

while again:
    result = 0
    operator_show = input("Pick an operation: ")
    operator_Chose = operator[operator_show]
    ask_2 = float(input("What's the next number?: "))
    if operator_Chose == add:
        result = add(n1=ask, n2=ask_2)
    elif operator_Chose == substract:
        result = substract(n1=ask, n2=ask_2)
    elif operator_Chose == divide:
        result = divide(n1=ask, n2=ask_2)
    elif operator_Chose == multiply:
        result = multiply(n1=ask, n2=ask_2)
    print(f"{ask} {operator_show} {ask_2} = {result}")
    ask = result
    continues = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ").lower()
    if continues == 'n':
        again = False
        print("Thank you to use the calculator, see you next times.")

# My teacher version
# from replit import clear
# from art import logo

# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# def multiply(n1, n2):
#   return n1 * n2

# def divide(n1, n2):
#   return n1 / n2

# operations = {
#   "+": add,
#   "-": subtract,
#   "*": multiply,
#   "/": divide
# }

# def calculator():
#   print(logo)

#   num1 = float(input("What's the first number?: "))
#   for symbol in operations:
#     print(symbol)
#   should_continue = True
 
#   while should_continue:
#     operation_symbol = input("Pick an operation: ")
#     num2 = float(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     answer = calculation_function(num1, num2)
#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
#       num1 = answer
#     else:
#       should_continue = False
#       clear()
#       calculator()

# calculator()
