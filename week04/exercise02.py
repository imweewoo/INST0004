#Animal Guesser Game

#Import libraries
import random

class Animal():

    """My animal is size 1-10 and is one of these species:"""

    #Initialse attributes
    def __init__(self, animal, size):
        self.animal = animal
        self.size = size

    #Show list of selectable species
    def show(self):
        speciesList = ["Bear", "Lion", "Tiger", "Monkey", "Crocodile"]

        #Print list
        for species in speciesList:
            print(species)

    def guess(self):
        count = 0 #Running count

        while count < 8:

            while True:
                #Species guess entry + validation if species not in list
                try:
                    speciesGuess = input(f"Try to guess the animal species: ").strip()
                    if speciesGuess.lower() != "bear" and speciesGuess.lower() != "lion" and speciesGuess.lower() != "tiger" and speciesGuess.lower() != "monkey" and speciesGuess.lower() != "crocodile" and speciesGuess.lower() != "done":
                        raise ValueError(f"Please enter one of the listed animals")
                    break
                except ValueError as error:
                    print(error)

            #species stop condition
            if speciesGuess.lower() == "done":
                print("Thank you for playing the game!")
                print("Goodbye :)")
                return

            while True:
                #size guess entry + validation if larger than 10
                try:
                    sizeGuess = int(input(f"Try to guess the animal size: "))
                    if sizeGuess > 10:
                        raise ValueError(f"Please enter a size between 1-10")
                    break
                except ValueError as error:
                    #integer error message
                    if "invalid literal" in str(error):
                        print("Enter an integer")
                    #size range error
                    else:
                        print(error)

            #size stop condition
            if sizeGuess <= 0:
                print("Thank you for playing the game!")
                print("Goodbye :)")
                return

            #Increase guess number
            count += 1

            #Check guesses
            self.compare(speciesGuess, sizeGuess)

        print("You've ran out of guesses. Please try again!!")

    def compare(self, speciesGuess, sizeGuess):

        #Check if animal species is wrong
        if self.animal != speciesGuess.lower():
            print("Wrong animal species!")

        #Check if size is right and print win condition if guessed correctly
        if sizeGuess < self.size:
            print("Too small.")
        elif sizeGuess > self.size:
            print("Too big.")
        elif self.animal == speciesGuess.lower() and sizeGuess == self.size:
            print("Perfect Match")
            print("Congratulations you won!")   
            return 


#Random size and species generation
randomAnimal = random.choice(["bear", "lion", "tiger", "monkey", "crocodile"])
randomSize = random.randint(1,10)

#Create object
animalObj = Animal(randomAnimal, randomSize)
print(animalObj.__doc__) #print text in class

#Show details and start guessing
animalObj.show()
animalObj.guess()