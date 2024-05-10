import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type: Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in option:
        continue

    random_number = random.randint(0, 2)
    # r:0, p:1, s:2
    computer_pick = option[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("You lost!")
        computer_wins += 1

print("You won, ", user_wins, " times.")
print("Computer won, ", computer_wins, " times.")
print("Goodbye!")


