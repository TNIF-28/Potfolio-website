balance = 0
amount = 0

while True:
    print("\n     \n")
    print("Welcome to your ATM Simulator")
    print("1.Check balance")
    print("2.Deposite money")
    print("3.Withdraw money")
    print("4.Exit")
    opera = int(input(print("Please enter the Number corresponding to the operation you want to carry out")))
    if opera == 1:
        print(f"Your account Balance is: {balance:,} Xaf")
    elif opera == 2:
        amnt = float(input(print("Enter the amount you want to deposite")))
        if amnt < 0:
            print("Amount can not be negative")
        else:
             balance += amnt
             print("Sucessful Deposite")
    elif opera == 3:
        withdraw = float(input(print("Enter the amount you want to withdraw")))
        if withdraw > balance:
           print("InSUFFICIANT AMOUNT IN ACCOUNT")
        else:
           balance -= withdraw
           print("SUCCESSFUL WITHDRAWAL")
    elif opera == 4:
        print("Thanks for using ATM Simulator see you next time")
        break
    else:
        print("Invalid credentials")
    