
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("Not divisible by zero")
except ValueError:
    print("Enter only numbers")
