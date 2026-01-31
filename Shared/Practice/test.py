user_marks_str = input("Enter the number: ")
user_marks = float(user_marks_str)

if user_marks >= 90:
    print("Grade is A")
elif user_marks >= 80 and user_marks < 90:
    print("Grade is B")
elif user_marks >= 70 and user_marks < 80:
    print("Grade is C")
elif user_marks >= 60 and user_marks < 70:
    print("Grade is D")
else:
    print("Grade is E")
