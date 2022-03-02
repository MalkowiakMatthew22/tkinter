from tkinter import *
import random

#Functions
def startStory():
    nounOne = nounOneEntry.get()
    nounTwo = nounTwoEntry.get()
    verbOne = verbOneEntry.get()
    verbTwo = verbTwoEntry.get()
    adjective = adjectiveEntry.get()
    nounOneLabel.destroy()
    nounTwoLabel.destroy()
    verbOneLabel.destroy()
    verbTwoLabel.destroy()
    adjectiveLabel.destroy()
    nounOneEntry.destroy()
    nounTwoEntry.destroy()
    verbOneEntry.destroy()
    verbTwoEntry.destroy()
    adjectiveEntry.destroy()
    startButton.destroy()
    storyLabel.config(text = "     There once was a " + nounOne + " that was very hungry and they had a deep and unreasonable hunger.\nThey thought, 'Wow, I could really go for a very " + adjective + 
    " " + nounTwo +" right now.'\n" + nounOne + " then " + verbOne + " out to the " + adjective + " " + nounTwo + 
    " store, " + verbTwo + " the cashier and " + verbOne + " back home. \n" + nounOne + " then finally, ate their " + adjective + 
    " " + nounTwo + " in peace.\n|THE END|")


#Window Setup
mainWindow = Tk()
mainWindow.geometry("900x200")
mainWindow.title("Madlib")
#Widgets and Word Inputs

nounOneLabel = Label(mainWindow, text = "Name")
nounTwoLabel = Label(mainWindow, text = "Noun")
verbOneLabel = Label(mainWindow, text = "Past Tense Verb")
verbTwoLabel = Label(mainWindow, text = "Past Tense Verb")
adjectiveLabel = Label(mainWindow, text = "Adjective")

nounOneLabel.grid(row = 1, column = 1)
nounTwoLabel.grid(row = 2, column = 1)
verbOneLabel.grid(row = 3,column = 1)
verbTwoLabel.grid(row = 4, column = 1)
adjectiveLabel.grid(row = 5, column = 1)

nounOneEntry = Entry(mainWindow)
nounTwoEntry = Entry(mainWindow)
verbOneEntry = Entry(mainWindow)
verbTwoEntry = Entry(mainWindow)
adjectiveEntry = Entry(mainWindow)

nounOneEntry.grid(row = 1, column = 0)
nounTwoEntry.grid(row = 2, column = 0)
verbOneEntry.grid(row = 3, column = 0)
verbTwoEntry.grid(row = 4, column = 0)
adjectiveEntry.grid(row = 5, column = 0)

#Start Seq; Button; Story Label

startButton = Button(mainWindow, text = "Click When Ready", command = lambda: startStory())
startButton.grid(row = 6, column = 0)

storyLabel = Label(mainWindow, text = "", font = "roman 14 bold")
storyLabel.grid(row = 0, column = 0)

mainWindow.mainloop()