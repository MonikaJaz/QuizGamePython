print("Welcome to my computer quiz!")

playing = input("Do you want ot play? ")

if playing.lower() != "yes":
    quit()
print("Okay let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Wrong answer!")


