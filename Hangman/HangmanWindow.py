from tkinter import *
from PIL import ImageTk,Image
import HangmanLogic

window = Tk()
window.title('Hangman')
window.geometry("500x400")

newText = ""
finalAnswer = ""
lives = 7

def printAnswer(args):
    global newText
    global finalAnswer
    global lives
    if args == 0:
        HangmanLogic.resetWordList()
        answer = wordEntry.get()
        finalAnswer = wordEntry.get()
        newText = HangmanLogic.getWord(answer)
        wordEntry.delete(0,END)
        wordButton['state'] = 'disabled'
        wordEntry['state'] = 'disabled'
        guessLetterButton['state'] = 'normal'
        guessLetterEntry['state'] = 'normal'
        guessWordButton['state'] = 'normal'
        guessWordEntry['state'] = 'normal'
        emptySpaces.config(text=newText)
    elif args == 1:
        answer = guessLetterEntry.get()
        guessLetterEntry.delete(0,END)
        newText = HangmanLogic.checkLetter(answer)
        if(newText == "incorrect"):
            lives -= 1
            changePic()
            livesLabel.config(text="Lives: " + str(lives))
            if(lives == 0):
                livesLabel.config(text="Game Over: You Ran Out Of Lives")
                disableThings()
                emptySpaces.config(text="The Word Was: " + finalAnswer)
        else:
            emptySpaces.config(text=newText)
            if("_" not in emptySpaces['text']):
                livesLabel.config(text="You Guessed Word Correctly")
                disableThings()

    elif args == 2:
        answer = guessWordEntry.get()
        guessWordEntry.delete(0,END)
        newText = HangmanLogic.checkWord(answer)
        if(newText == "incorrect"):
            lives = 0
            changePic()
            livesLabel.config(text="Game Over: You Guessed The Wrong Word")
            disableThings()
            emptySpaces.config(text="The Word Was: " + finalAnswer)
        else:
            emptySpaces.config(text=newText)
            if(answer == finalAnswer):
                livesLabel.config(text="You Guessed Word Correctly")
                disableThings()

def disableThings():
    wordButton['state'] = 'disabled'
    wordEntry['state'] = 'disabled'
    guessLetterButton['state'] = 'disabled'
    guessLetterEntry['state'] = 'disabled'
    guessWordButton['state'] = 'disabled'
    guessWordEntry['state'] = 'disabled'

def changePic():
    global lives
    if(lives == 7):
        imageLabel.config(image=image0)
    elif(lives == 6):
        imageLabel.config(image=image1)
    elif(lives == 5):
        imageLabel.config(image=image2)
    elif(lives == 4):
        imageLabel.config(image=image3)
    elif(lives == 3):
        imageLabel.config(image=image4)
    elif(lives == 2):
        imageLabel.config(image=image5)
    elif(lives == 1):
        imageLabel.config(image=image6)
    else:
        imageLabel.config(image=image7)
    

image0 = ImageTk.PhotoImage(Image.open("Hangman.png"))
image1 = ImageTk.PhotoImage(Image.open("Hangman1.png"))
image2 = ImageTk.PhotoImage(Image.open("Hangman2.png"))
image3 = ImageTk.PhotoImage(Image.open("Hangman3.png"))
image4 = ImageTk.PhotoImage(Image.open("Hangman4.png"))
image5 = ImageTk.PhotoImage(Image.open("Hangman5.png"))
image6 = ImageTk.PhotoImage(Image.open("Hangman6.png"))
image7 = ImageTk.PhotoImage(Image.open("Hangman7.png"))
imageLabel = Label(image=image0)
imageLabel.pack(side=LEFT)

livesLabel = Label(window, text="Lives: 7", font="Arial 25")
livesLabel.pack()

emptySpaces = Label(window, text="", font="Arial 40")
emptySpaces.pack()

wordButton = Button(window, text="Enter A Word", command=lambda:printAnswer(0))
wordButton.pack()
wordEntry = Entry(window)
wordEntry.pack()

guessLetterButton = Button(window,state = "disabled", text="Guess A Letter", command=lambda:printAnswer(1))
guessLetterButton.pack()
guessLetterEntry = Entry(window,state = "disabled")
guessLetterEntry.pack()

guessWordButton = Button(window,state = "disabled", text="Guess The Word", command=lambda:printAnswer(2))
guessWordButton.pack()
guessWordLabel = Label(window, text="You get one try to guess the word.", font="Arial 10")
guessWordLabel.pack()
guessWordEntry = Entry(window,state = "disabled")
guessWordEntry.pack()

def resetWindow():
    global newText
    global finalAnswer
    global lives

    newText = ""
    finalAnswer = ""
    lives = 7

    changePic()
    livesLabel.config(text="Lives: " + str(lives))
    HangmanLogic.resetWordList()
    emptySpaces.config(text="")
    wordEntry.delete(0,END)
    guessLetterEntry.delete(0,END)
    guessWordEntry.delete(0,END)
    wordButton['state'] = 'normal'
    wordEntry['state'] = 'normal'
    guessLetterButton['state'] = 'disabled'
    guessLetterEntry['state'] = 'disabled'
    guessWordButton['state'] = 'disabled'
    guessWordEntry['state'] = 'disabled'

exitButton = Button(window, text="Exit", command=window.destroy).pack(side=BOTTOM, pady=5)
reset = Button(window, text='Reset', command=resetWindow).pack(side=BOTTOM)

window.mainloop()
