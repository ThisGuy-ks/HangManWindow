word = ""
wordList = []
guess = ""
wordReturn = ""

def getWord(wordToBeGuessed):
    global word
    word = wordToBeGuessed.lower()

    for x in range(len(word)):
        if(word[x] != " "):
            wordList.append("_")
        else:
            wordList.append(" ")

        wordReturn = ' '.join(wordList)
    return wordReturn

def resetWordList():
    wordList.clear()


def checkLetter(le):
    correct = False
    guess = le.lower()
    for x in range(len(word)):
        if word[x] == guess:
            wordList[x] = guess
            correct = True
    if(correct):
        wordAndDashes = ' '.join(wordList)
        return wordAndDashes
    else:
        return "incorrect"

def checkWord(wo):
    guess = wo.lower()
    if word == guess:
        return word
    else:
        return "incorrect"
