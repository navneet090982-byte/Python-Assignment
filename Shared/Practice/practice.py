def number_check(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


number_check(int(input("Enter the number: ")))


def func(**kwargs):
    print(kwargs)


func(x=10, y=20)
