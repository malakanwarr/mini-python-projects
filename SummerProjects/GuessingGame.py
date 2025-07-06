import random

print("Welcome to our Guessing Game! You have a limit of 10 tries")
print("Choose Difficulty Mode: ")
print("Easy: 1–50, , Hard: 1–200")
choice= input("Your choice: ")
n = 10
tries=1
if choice == "Easy":
    r = random.randint(1,50)
elif choice == "Hard":
    r = random.randint(1,200)
else:
    r = random.randint(1,100)

while True:
    if n>0:
        a=input("GUESS!! : ")
        if int(a)==r:
            print("YOU'VE GUESSED IT CORRECTLY IN " + str(tries) + " TRIES!!!")
            break
        elif int(a)>r:
            print("too highhh!!")
        elif int(a)<r:
            print("too low!!")
        tries+=1
        n-=1
    else:
        print("Game Over! You lost all your tries")
        break





