name = input("Type your name: ")
print("Welcome ", name, " to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer == input("You come to a river, you can walk around or swim across? Type 'walk' to walk around and 'swim' to swim across: ").lower()
    if answer == 'swim':
        print("You swam across and were eaten by an alligator.")
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and you lost the game!")
    else:
        print("Not a valid option. You lost!")
elif answer == "right":
    answer= input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ")
    if answer == 'back':
        print("You went back and lost!")
    elif answer == 'cross':
        answer = input("You crossed the bridge and met a stranger, Do you talk to him? (yes/no) ")
        if answer == "yes":
            print("You talked to the stranger and he gave you gold. You won!")
        elif answer == "no":
            print("You were killed by the stranger because you ignored him.")
        else:
            print("Not a valid option. You lost!")
    else:
        print("Not a valid option. You lost!")
else:
    print("Not a valid option. You lost!")

print("Thank you for trying,",name)
