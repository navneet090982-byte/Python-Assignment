'''
Docstring for Assignment5_1

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
'''


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
