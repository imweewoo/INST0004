#Number Guesser Program

#Import libraries
import random

def main():
    #Generate random number + guesses
    randomNumber = random.randrange(1,101)
    guess = 0
    win = False

    #Opening message
    print("The number is between 1 and 100.")
    print("You are allowed 5 guesses.")

    #5 guess limited loop
    while guess != 5:

        #Integer validation
        while True:
            try:
                num = int(input("Enter your guess: "))
                break
            except ValueError:
                print(f"Enter an integer")

        #Size checker
        if num > randomNumber:
            print(f"Too high!")
            guess += 1
            print(f"You have {5-guess} guesses remaining.")
        elif num < randomNumber:
            print(f"Too low!")
            guess += 1
            print(f"You have {5-guess} guesses remaining.")
        elif num == randomNumber:
            print(f"Correct! You used {guess+1} guesses")
            win = True
            break

    #Lose message
    if guess == 5 and win == False:
        print(f"You have exceeded your allowed number of guesses! The correct number was: {randomNumber}")
        
main()