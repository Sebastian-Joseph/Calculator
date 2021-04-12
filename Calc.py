import math

a = None
b = None
op = None

def add(a, b):
   return a + b

def sub(a, b):
   return a - b

def mult(a, b):
   return a * b

def div(a, b):
   return a / b

def avg(a, b):
   return ((a+b)/2)

def power(a, b):
   return a**b

def sqrt(a):
   return math.sqrt(a)



while (True):
    a = input("Enter the first number: ").lower()
    op = input("Enter the operation: ").lower()
    b = input("Enter the second number: ").lower()
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument..")
        op = None

    if op != None:
        if op == "+":
            print("Sum: ", add(a, b))
        elif op == "-":
            print("Difference: ", sub(a, b))
        elif op == "*":
            print("Product: ", mult(a, b))
        elif op == "/":
            print("Quotient: ", div(a, b))
        elif op == "avg":
            print("Average: ", avg(a, b))
        elif op == "power":
            print("Product: ", power(a, b))
        elif op == "sqrt":
            print("Answer: ", sqrt(a))
        else:
            print("Invalid Operation")

    choice = input("Do you want to quit? [y/n]: ").lower()
    if choice == "y" or choice == "Y":
        break


