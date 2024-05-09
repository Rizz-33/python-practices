print("Welcome For The Quiz !")

playing = input("Wanna play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's go")
score = 0

answer = input("Which software design pattern involves wrapping classes to add new functionalities? ")
if answer.lower() == "decorator":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the method of software development that uses iterative cycles and collaborative teamwork? ")
if answer.lower() == "agile":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the term for the structured approach used to manage projects and software development? ")
if answer.lower() == "waterfall":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the term for the repository system used to manage source code versions? ")
if answer.lower() == "git":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Congrats! you got " + str(score) + " questions correct!")
print("Congrats! you got " + str((score/4)*100) + "%.")