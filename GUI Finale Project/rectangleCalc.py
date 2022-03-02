from tkinter import *

def init():
    
    def Calculate():
        a = int(side1Entry.get()) * int(side2Entry.get()) 
        answerLabel.config(text = a)
    
    mainWindow = Tk()
    mainWindow.geometry("300x100")
    mainWindow.title("Area Of Rectangles")
    
    
    #Area Calculations
    side1Label = Label(mainWindow, text = "SIDE 1", font = "roman 14 bold")
    side1Label.grid(row=0, column=0)
    
    side2Label = Label(mainWindow, text = "SIDE 2", font = "roman 14 bold")
    side2Label.grid(row=0, column=1)
    
    side1Entry = Entry(mainWindow)
    side1Entry.grid(row=1, column=0)
    
    side2Entry = Entry(mainWindow)
    side2Entry.grid(row=1, column=1)
    
    calcButton = Button(mainWindow, text = "Calculate Area", command = lambda: Calculate())
    calcButton.grid(row = 2, column = 0)
    
    answerLabel = Label(mainWindow, text = "")
    answerLabel.grid(row = 2, column = 1)
    mainWindow.mainloop()