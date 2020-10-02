n = 3

guess = int(input("Please choose a number between 1 and 5: "))

while guess != n:
    if guess > n:
        print("Too high, try again.")
    elif guess < n:
        print("Too low, try again.")

    guess = int(input("Enter your guess: "))

print("Correct!")