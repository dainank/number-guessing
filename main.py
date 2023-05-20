import random

def guessing_game():
    inclusiveLowerBound = 0
    exclusiveUpperBound = 100
    randomInteger = random.randint(inclusiveLowerBound, exclusiveUpperBound)
    totalGuesses = 0
    print("I have generated a number between 0 and 100 (inclusive).")

    while totalGuesses < 5:
        try:
            userResponse = int(input("Guess the number: "))
        except:
            print("This was not a number. Please input an integer.")
            continue

        if (userResponse == randomInteger):
            print("Correct guess! Match found. Exiting...")
            return
        else:
            totalGuesses += 1
            if (userResponse > randomInteger):
                print("Too high!")
            elif (userResponse < randomInteger):
                print("Too low!")
    print("All guesses used! (5) Exiting...")

guessing_game()
