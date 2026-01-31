

chance = 1
correct_number = 25
attempts = 10


while chance <= 10:
    print(f"You have {attempts} chances left")
    number = int(input("Enter the number: "))
    if number == correct_number:
        print("Correct number")
        break
    else:
        if number < correct_number:
            higher = "Higher"
            print(f"Number is different. Go {higher}")
        else:
            higher = "Lower"
            print(f"Number is different. Go {higher}")

    chance += 1
    attempts -= 1

print("Game Over")
