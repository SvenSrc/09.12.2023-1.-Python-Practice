import random

print("Enter a number")
first = input()
print("\n")

print("Enter a second number")
second = input()
print("\n")

print("Guess the number between " + first + " and " + second + "\n")

randomNumber = random.randint(int(first), int(second))

guessing = True

while guessing:
    numberGuessing = int(input())
    if numberGuessing == randomNumber:
        guessing = False
        print("Correct, the number was: " + str(randomNumber))
    else:
        print("Try Again \n")


