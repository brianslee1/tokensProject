def tokenizeMySentence(sentence):
    results = sentence.split()
    # returns the sentence into seperate elements in an array
    return results

def getAlphaNumericWords(sentence):
    results = []
    words = tokenizeMySentence(sentence)
    for word in words:
        if word.isalnum():
            results.append(word)
    return results
    
def writeToFile(sentence):
    fpw = open("temp.txt", "a+")
    normalwords = getAlphaNumericWords(sentence)
    for word in normalwords:
        fpw.write(word)
        fpw.write("\n")
    fpw.close()

def main():
    sentence = ""
    while sentence != "-1":
        sentence = input("Type in a sentence: ")
        print(sentence)
        writeToFile(sentence)

if __name__ == "__main__":
    main()











"""

def getPi():
    return 3.14
    
def main():
    mySentence = "I like eating breakfast #@ 9042 *#@."
    tokens_list = mySentence.split()
    print(tokens_list)



    
    fpw = open("temp.txt", "w+")
    fpw.write("It's winter break!")

    # Write the tokens from tokens_list into temp.txt (12/19/2020)

    fpw.close()


if __name__ == "__main__":
    main
"""