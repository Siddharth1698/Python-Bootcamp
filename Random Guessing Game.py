import random

print("Guess a number between 1 and 100")
num = random.randrange(1, 100)
guess = int(input("Guess: "))
tries = 1

while guess != num:
    if guess > num:
        print("Little Lower")
    else:
        print("Little Higher")

    guess = int(input("Guess Again"))
    tries = tries + 1

print("you guessed it right. The num was", num)

