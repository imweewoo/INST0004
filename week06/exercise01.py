#Counting word program

def recursiveWordCount(words, counted_word):
    for word in words:
        if word == counted_word:
            return 1 + recursiveWordCount(words, counted_word)
        elif word != counted_word:
            return 0 + recursiveWordCount(words, counted_word)
    return 0


def main():  
    #String entry
    counted_word = input("Enter a single word to count: ")
    sentence = input("Enter a sentence ending with a (.): ")

    #Convert to lowercase
    counted_word = counted_word.lower()
    sentence = sentence.lower()

    #Split the sentence words
    words = []
    for w in sentence.split():
        words.append(w.strip(".,"))
    words = iter(words)

    #Call recursion + print result
    count = recursiveWordCount(words, counted_word)
    print(f"The sentence has {count} instance of the word '{counted_word}'")

main()
