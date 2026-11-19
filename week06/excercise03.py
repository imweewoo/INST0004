#scrabble scores game

class ScrabbleGame:

    #Points dictionary
    points = {
            'd': 2, 'g': 2,
            'b': 3, 'c': 3, 'm': 3, 'p': 3,
            'f': 4, 'h': 4,  'v': 4, 'w': 4, 'y': 4,
            'k': 5,
            'j': 8, 'x': 8,
            'z': 10, 'q': 10,
            'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1,
            'r': 1, 's': 1, 't': 1, 'u': 1
            #points for the word: python = 3 + 4 + 1 + 4 + 1 + 1 = 14
            }

    def score(self, word):
        #Base case
        if len(word) ==0:
            return 0
        elif word[0] == '_':
            #_ scores 0
            return 0 + self.score(word[1:])
        else:
            #Return point value and rest of word
            return self.points[word[0]] + self.score(word[1:])

    def vowel(self, word):
        #Base case
        if len(word) ==0:
            return 0
        elif word[0] in 'aeiou':
            #Add score if vowel
            return 1+ self.vowel(word[1:])
        else:
            #Do not add score if consonant
            return 0+ self.vowel(word[1:])

    def isValid(self, word):
        #Check if there are any not allowed characters in the word
        for char in word:
            if char not in self.points and char != '_':
                return False
        return True

def main():
    #Create object
    game = ScrabbleGame()

    while True:
        #word validation
        try:
            #lowercase word input with no extra spaces
            word = input("Enter a word: ").lower().strip()
            valid = game.isValid(word)
            if valid is False:
                raise ValueError(f"Please enter a true word with or without underscores. NO other number or character allowed.")
            break
        except ValueError as error:
            print(error)

    #Output score and vowel count
    print(f"The scrabble score of '{word}' is {game.score(word)}.")
    print(f"'{word}' contains {game.vowel(word)} vowels.")
    
main()
    
