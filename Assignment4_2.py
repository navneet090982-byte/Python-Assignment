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
