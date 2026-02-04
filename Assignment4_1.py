'''
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''

with open("Sample.txt", 'wt') as file:
    file.write("This is a sample text file. \n")
    file.write("It contains multiple lines.")

try:
    with open("Sample.txt", "r") as fh:
        for i in fh:
            print(i.strip())
except FileNotFoundError:
    print("Error: The file does not exist")
