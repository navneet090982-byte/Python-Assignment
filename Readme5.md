Assignment 5

Task 1

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.


students = {"Amit": {"Math": 85, "English": 92, "Science": 98},
            "Varun": {"Math": 95, "English": 96, "Science": 93},
            "Mayank": {"Math": 100, "English": 90, "Science": 99},
            "Gautam": {"Math": 85, "English": 75, "Science": 60}}

while True:
    search_stu = input("Enter student's Name: ").strip().title()

    if search_stu in students:
        print("\nStudent Found !!!")

        for subject, marks in students[search_stu].items():
            print(f"{search_stu} marks in {subject} is {marks}")
    else:
        print("Student not found !!!")

    choice = input("Do you want to search again. Select Y/N: ")

    if choice == "N":
        print("OK. Run program again to search")
        break


Output
Enter student's Name: Navneet
Student not found !!!
Do you want to search again. Select Y/N: Y 
Enter student's Name: Amit

Student Found !!!
Amit marks in Math is 85
Amit marks in English is 92
Amit marks in Science is 98

Task 2

'''
Docstring for Assignment5_2

Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

'''

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(original_list))

print(f"Original list is: {original_list}",)

firstfive = original_list[:5]
print(f"Extracted first five elements: {firstfive}")
reversed_list = firstfive[::-1]
print(f"Reversed extracted elements: {reversed_list}")

Output

<class 'list'>
Original list is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]