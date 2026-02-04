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


Output:
This is a sample text file.
It contains multiple lines.

Task 2
'''
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
try:
    with open("Output.txt", "r") as file:
        print("File exist. Below are the contents: \n")
        print(file.read())
except FileNotFoundError:
    with open("Output.txt", "w") as file:
        data1 = input("Enter the text to write in file: ")
        file.write(data1 + "\n")
        print("Data successfully written to Output.txt")
except FileExistsError:
    with open("Output.txt", "at") as file:
        new_input = input("Enter additional text to append: ")
        file.write(new_input + "\n")
        print("Data Successfully Appended")

with open("Output.txt", "at") as file:
    new_input = input("Enter additional text to append: ")
    file.write(new_input + "\n")
    print("Data Successfully Appended")

with open("Output.txt", "r") as fh:
    print("Final content of output.txt is: ")
    print(fh.read())

Output:

Enter the text to write in file: Hello Python !!!
Data successfully written to Output.txt
Enter additional text to append: Learning file handling in python.
Data Successfully Appended
Final content of output.txt is:
Hello Python !!!
Learning file handling in python.