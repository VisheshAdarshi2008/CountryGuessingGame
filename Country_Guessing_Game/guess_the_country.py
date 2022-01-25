'''Country guessing game made using python tkinter'''
# importing the modules that are required
from tkinter import *
from random import choice
from random import shuffle
#
'''
This is a word jumble game in which you will be given a string of country name and you have to guess it correctly.
'''

# setting properties of window
root = Tk()
# setting window size
root.geometry("1000x600")
# setting window color
root.config(bg="light green")
# setting window title
root.title("Country Guessing Game!!!!")

heading = Label(root, text="Country Guessing Game", font=("Consolas",35), bg="light green")
heading.pack()
# label for showing the jumbled word
lbl1 = Label(root, text="", font=("Consolas",48), bg="light green")
lbl1.pack(pady=20)

# function for shuffling and picking a word
def shuffler():
    #
    hintLabel.config(text='')
    global hint_count
    hint_count = 0
    entryAnswer.config(text='')

    #file handling
    # Countries.txt has list of names of countries
    # we are picking one word from txt file that will be guessed by the user
    country = open("Countries.txt",'r').read().splitlines()
    # variable for storing the word to be guessed
    global word
    word = choice(country)
    breakWord = list(word)
    # shuffling the letters of word
    shuffle(breakWord)

    global shuffleWord
    shuffleWord = ''
    for letter in breakWord:
        shuffleWord += letter
    lbl1.config(text=shuffleWord)

# function for checking the answer of user
def answer():
    # checking whther user guess is correct or not
    if word == entryAnswer.get():
        answerLabel.config(text="Correct Answer!!")
    else:
        answerLabel.config(text="Incorrect Answer!!")

global hint_count
hint_count = 0

# function for checking whether the user has reached his limit of hints
def hint(count):
    global hint_count
    hint_count = count
    word_length = len(word) - 4

    if count < word_length:
        hintLabel.config(text = f'{hintLabel["text"]} {word[count]}')
        hint_count += 1

# entry box for user guess
entryAnswer = Entry(root, font=("Consolas",28), bg="light blue", fg="black",  relief=FLAT, borderwidth=14, border=10)
entryAnswer.pack(pady=28)

# frame for buttons
btnFrame = Frame(root, bg="light green")
btnFrame.pack(pady=20)

# submit button for checking answer of user
answerButton = Button(btnFrame, text="Submit", relief=RIDGE, width=15, font=("Consolas",15), height=2, borderwidth=5, bg="light blue", command=answer)
answerButton.grid(row=0, column=0, padx=10)
# button for changing word
anotherWordButton = Button(btnFrame, text="Pick another word", relief=RIDGE, font=("Consolas",15), width=20, height=2, borderwidth=5, bg="light blue", command=shuffler)
anotherWordButton.grid(row=0, column=1, padx=10)
# button for geting the hint
hintButton = Button(btnFrame, text="Hint", width=15 , relief=RIDGE, font=("Consolas",15), height=2, borderwidth=5, bg="light blue", command=lambda: hint(hint_count))
hintButton.grid(row=0, column=2, padx=10)

# label for showing wheteher the user is correct or not
answerLabel  = Label(root, text='', font=('Consolas',20), bg="light green")
answerLabel.pack(pady=20)
# label for showing hint
hintLabel = Label(root, text='', font=('Consolas',20), width=25, bg="light green")
hintLabel.pack(pady=20)

# function call
shuffler()
# running the mainloop
root.mainloop()