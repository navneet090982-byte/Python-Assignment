
balance = 0


def check_balance():
    print("*************************************")
    print(f"Your current balance is {balance}")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Amount cannot be less than zero")


def withdrawl(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw a negative amount")
    elif amount > balance:
        print("Insufficient funds")

    balance -= amount


print("*******************************")
print("Welcome to Your Bank !!!")
print("********************************")

while True:
    print("1. Check you Balance")
    print("2. Deposit an account")
    print("3. Withdraw an amount")
    print("4. Quit")
    print("****************************")
    choice = int(input("Enter the desired number: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        print("**************************")
        amount = float(input("Enter the amount you need to deposit: "))
        deposit(amount)
    elif choice == 3:
        print("***************************")
        amount = float(input("Enter the amount you need to Withdraw: "))
        withdrawl(amount)
    elif choice == 4:
        break
    else:
        print("Invalid Choice. Retry")

print("************************************")
print("Thank you for banking with Bank !!!")
print("************************************")
