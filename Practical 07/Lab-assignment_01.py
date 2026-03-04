# Create a Menu Driven application "CALC" by implemnting different functions for the following basic operations:
# a) Addition
# b) Subtraction
# c) Multiplication
# d) Division
# e) Modulus

# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero not allowed"
    return a / b

def modulus(a, b):
    return a % b

# Menu
print("------ CALC MENU ------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter your choice (1-5): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
elif choice == 5:
    print("Result:", modulus(num1, num2))
else:
    print("Invalid choice")