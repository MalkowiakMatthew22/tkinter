from tkinter import *
import random

def init():

    #Functions
    def rtd():
        r = random.randrange(int(minEntry.get()), int(maxEntry.get()) + 1)
        answerLabel.config(text = r)
        
    
    #Window Setup
    mainWindow = Tk()
    mainWindow.geometry("300x100")
    mainWindow.title("Temple of RNGesus")
    #Widgets
    
    minLabel = Label(mainWindow, text = "MIN", font = "roman 14 bold")
    minLabel.grid(row = 0, column = 0)
    
    maxLabel = Label(mainWindow, text = "MAX", font = "roman 14 bold")
    maxLabel.grid(row = 0, column = 1)
    
    minEntry = Entry(mainWindow)
    minEntry.grid(row = 1, column = 0)
    
    maxEntry = Entry(mainWindow)
    maxEntry.grid(row = 1, column = 1)
    
    rollButton = Button(mainWindow, text = "PRAY TO HIM", command = lambda: rtd())
    rollButton.grid(row = 2, column = 0)
    
    answerLabel = Label(mainWindow, text = "", font = "roman 14 bold")
    answerLabel.grid(row = 2, column = 1)
    
    mainWindow.mainloop()