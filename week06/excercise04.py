#string manipulation

class StringTester:
    def display(self, word):
        print(f"The first character is: {word[0]}")
        print(f"The third character is: {word[2]}")
        print(f"The last character is: {word[-1]}")

        half = len(word)//2
        print(f"The second half of the word is: {word[half:]}")

def main():
    while True:
        #word length validation
        try:
            word = input("Enter a word that is at least 6 characters: ").strip()
            if len(word) < 6:
                raise ValueError(f"Enter a word at least 6 characters long")
            break
        except ValueError as error:
            print(error)
    #Create object and display
    tester = StringTester()
    tester.display(word)

main()