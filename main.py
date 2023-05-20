import random

def guessing_game():
    inclusiveLowerBound = 0
    exclusiveUpperBound = 100
    randomInteger = random.randint(inclusiveLowerBound, exclusiveUpperBound)
    print("I have generated a number between 0 and 100 (inclusive).")

    while True:
        userResponse = int(input("Guess the number: "))
        if (userResponse > randomInteger):
            print("Too high!")
        elif (userResponse < randomInteger):
            print("Too low!")
        elif (userResponse == randomInteger):
            print("Correct guess! Match found. Exiting...")
            return
        else:
            print("This was not a number. Please input an integer.")

guessing_game()
