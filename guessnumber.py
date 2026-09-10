import random

number = random.randint(1, 10)

print("🎮 Guess the Number (1-10)")

while True:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Correct! You win!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")