balance = 1000

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Balance:", balance)

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")

# Output:
# 1.Deposit
# 2.Withdraw
# 3.Check Balance
# 4.Exit
# Enter choice: 1
# Enter deposit amount: 500
# Balance: 1500
# Enter choice: 4
# Thank You
