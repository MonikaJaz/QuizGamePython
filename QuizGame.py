print("Welcome to my computer quiz!")

playing = input("Do you want ot play? ")

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Wrong answer!")
print("You got" + str(score) + "questions correct!")
print("You got " + str(score/4 * 100) + "%")





