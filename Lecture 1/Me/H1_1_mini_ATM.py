balance = float(input("How much balance do you have? "))
withdraw_amount = float(input("Enter the amount of money you want to withdraw: "))
if withdraw_amount <= balance:
    print("Withdrawal was successful")
    print(f"Remaining balance: {balance - withdraw_amount}")
else:
    print("Insufficient balance!")
if balance < 0:
    print("Invalid balance!")