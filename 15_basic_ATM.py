# Initial balance
balance = 1000

def check_balance():
    print("Your current balance is: $", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited $", amount)
    check_balance()

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print("Withdrew $", amount)
        check_balance()

def atm_simulation():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Start the ATM simulation
atm_simulation()
