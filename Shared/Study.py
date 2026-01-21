s1 = "Hello world"
print(s1)

# find length of string
print(len(s1))

# indexing
print("First Character", s1[0])
s1 = "Hello World"
print("Last character", s1[-1])
s1 = "Hello World"
print(s1[1:7:1])
print(s1[2:8:2])
print(s1[0:10:3])
print(s1[1:12:3])


name = "John"

sub1 = 78
sub2 = 87
sub3 = 83

Total = sub1 + sub2 + sub3
percentage = (sub1 + sub2 + sub3)/3
print(f"{name} scored {sub1 + sub2 + sub3} in total.")
print(f"{name} percentage is {round(percentage, 2)} %")

# \n pracice
print("Hellow Navneet. \n Are you learning python")
# \t practice
print("Hi,\t How are you")

print('This is Navneet\'s work')


s1 = "Strip    "
s2 = s1.strip()
print(s2)

print("Python" == "Python")
print("Python   " == "Python")

print(("Python   ").strip() == "Python")


s1 = "We are learning Python"

print(s1)
print(s1.replace("Python", "Java"))

print(s1.replace("a", "A", 1))


s1 = "We are learning Python. Python is fun"
print(s1.count("Python"))

print(f"Occurance of Python is {s1.count("Python")}")


name = "John"
age = 20
percentage = 85.5

student = ["John", 20, 85.5]
print(type(student))


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(len(days))
print(f"Last day of week is {days[6]}")
print(f"Last day of week is {days[-1]}")

lis = [2, 8, 3, 5, 6, 7, 6, 9, 2]
print(len(lis))

# slicing
print(lis[1:8:1])

l1 = [2, 4, 6, 8, 10, 12, 14]
print(l1[1:3:1])
print(l1[1:8:2])

l1 = [1, 2, 3]
l2 = [0, 5]

print(l1+l2)
print(l1*2)

fruits = ["Mango", "Banana", "Orange"]
fruits.append("Apple")
print(fruits)
fruits.insert(0, "Kiwi")
print(fruits)
fruits.insert(3, "Sapota")
print(fruits)

fruits.append(["Pineapple", "Papaya"])
print(fruits)


list_nested = [5, 5.5, "Python", True, None, [1, 2, 3], 10]

print(list_nested[-2])
print(list_nested[-2][1])

l2 = [[1, 2], [3, 4], [5, 6, [0, 1]]]
print(l2[2])
print(l2[2][2][0])

l1 = [10, 30, "Python"]
print(type(l1))

l1 = (10, 30, "Python")
print(type(l1))

l1 = {10, 30, "Python", 10}
print(type(l1))
print(l1)


num1 = {1, 3, 0, 1}
print(3 in num1)

num2 = {4, 6, 8}

print(num1 + num2)

weekday = ("Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun")
print(type(weekday))
weekday = set(weekday)
print(type(weekday))
print(weekday)

weekday.add("January")
print(weekday)


st1 = {"Eng", "Math", "Bio", "Phy"}
st2 = {"Eng", "Comp", "Bio", "Phy"}

print(st1, type(st1))

day1 = {"Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"}
weekend = {"Sat", "Sun"}


st1_marks = {'Eng': 20, 'Math': 50, 'Phy': 60}
print(st1_marks, type(st1_marks))
print(st1_marks["Phy"])
print(st1_marks.get('Chem'))

groc1 = {'Milk': 60, 'Rice': 100, 'Bisc': 100}
groc2 = {'Rice': 200, 'Bread': 50}

groc1.update(groc2)
print(groc1)


groc1 = {'Milk': 60, 'Rice': 100, 'Bisc': 100}
groc2 = {'Rice': 200, 'Bread': 50}

groc1.pop('Rice')
print(groc1)

d1 = ['Mike', 10.2, 1980]
for i in d1:
    print(i)

if condition:
    Statement1
    Statement2
    .
    .
    StatmentN
StatementM

age = float(input("Enter age"))
if age >= 18:
    print("You are eligible to vote.")


# marks >== 90, grade A
# marks 80 and 89 , Grade B
# marks 70 and 79, Grade C
# marks 60 and 69, Grade D
# marks < 60 , Grade E
