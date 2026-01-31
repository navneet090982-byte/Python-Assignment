import random
for i in range(20, 10, -1):
    print(i)


scores = [2, 45, 55, 69, 2, 100, 40, 36, 26]
print(len(scores))

F_score = 0
for i in scores:
    F_score = F_score + i
print(f"Total run scored is {F_score}")


scores = [2, 45, 55, 69, 2, 100, 40, 36, 26]
total = sum(scores)
print(total)


print(random.randint(10, 15))


for i in range(6):
    for j in range(1, i+1):
        print("*", end="")
    print()

# Roll a dice
# No of face in dice 1 - 6
# Program randamoly print 1- 6


print("Welcome to game of Dice. Roll the dice")

while True:
    choice = input("Press 'R' to roll dice or 'Q' to quit: ")
    if choice == 'Q':
        print("Thanks for the game. BYE !!!")
        break
    elif choice == 'R':
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else:
        print("Invalid Input")

print("Game Over!!!")


Countries = ["India", "USA", "Iran", "Australia", "Ireland", "Cuba"]

counter = 0
output_c = []
for i in Countries:
    if Countries[0] == "I":
        counter = counter + 1
        output_c = output_c.append(Countries)

print(counter)
