# Create a Menu Driven program for showing details of a Bank Account by implementaing different functions for the following:
# a) Display the current Balance
# b) Mechanism to Deposit an amount
# c) Mechanism to Withdraw an amount

# Initial balance
balance = 1000

# Function to display balance
def display_balance():
    print("Current Balance:", balance)

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited Successfully")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

while True:
    print("\n------ BANK MENU ------")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using the bank system")
        break
    else:
        print("Invalid Choice")