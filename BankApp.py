class Account:
    def __init__(self, name, id_no, account_no):
        self.name = name
        self.id_no = id_no
        self.account_no = account_no
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance is: ${self.balance}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Account balance is: ${self.balance}")


# Gather basic account info from the user
name = input("Enter name: ")
id_no = input("Enter ID number: ")
account_no = input("Enter account number: ")

# Create the account
customer = Account(name, id_no, account_no)

# Let the user perform actions
while True:
    action = input("\nChoose an action - Deposit (D), Withdraw (W), Check Balance (B), or Exit (E): ").upper()
    
    if action == 'D':
        amount = float(input("Enter deposit amount: "))
        customer.deposit(amount)
    elif action == 'W':
        amount = float(input("Enter withdrawal amount: "))
        customer.withdraw(amount)
    elif action == 'B':
        customer.check_balance()
    elif action == 'E':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose D, W, B, or E.")
