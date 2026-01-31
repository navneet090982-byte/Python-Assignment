# Problem Statement:  Write a Python program that:
# 1. Takes an integer input from the user.
# 2. Checks whether the number is even or odd using an if-else statement.
# 3. Displays the result accordingly.

my_num = input("Enter the number: ")
my_num = int(my_num)

if my_num % 2 == 0:
    print(f"{my_num} is an even number")
else:
    print(f"{my_num} is an odd number")
