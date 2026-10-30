#Character Counting

class DotStar:
    #Assign values to object properties
    def __init__(self, dotCharacter, starCharacter):
        self.dotCharacter = dotCharacter
        self.starCharacter = starCharacter

    def display(self):
        sentence = input("Enter a sentence: ")
        
        #Loop while finish is not entered
        while sentence.lower() != "finish":
            dotCount = 0
            starCount = 0

            #Dot + star counter
            for i in sentence:
                if i == self.dotCharacter:
                    dotCount += 1

            for i in sentence:
                if i == self.starCharacter:
                    starCount += 1

            #Count outputs
            print(f"The character '{self.dotCharacter}' appears {dotCount} times.")
            print(f"The character '{self.starCharacter}' appears {starCount} times.")

            sentence = input("Enter a sentence: ")

        print("Goodbye! Good to see you!")

#Set symbols for the character variables
dotCharacter = '.'
starCharacter = '*'

#Create obejct + display
charObject = DotStar(dotCharacter, starCharacter)
charObject.display()