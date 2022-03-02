from tkinter import *

def init():

    mainWindow = Tk()
    
    photo1 = PhotoImage(file = "./Images/Bazinga.png").subsample(4)
    
    photoLabel = Label(mainWindow, image = photo1)
    photoLabel.pack()
    
    mainWindow.mainloop()