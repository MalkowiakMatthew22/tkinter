from tkinter import *
import mainMenu


showing = True



mainWindow = Tk()
def showHide():
    global showing

    if showing:
        passEntry.config(show = "*")
        showing = False

    else:
        passEntry.config(show = "")
        showing = True


def submit():
    if passEntry.get() == "Bazing4":
        successLabel.config(text = "ACcESS GRANTED", fg = "cornflowerblue")
        mainWindow.destroy()
        mainMenu.init()

    else:
        successLabel.config(text = "BAD, NO NO NO", fg = "red")
    
#Window Setup

mainWindow.geometry("400x100")
mainWindow.title("The Place At Which You Are Logging In")
mainWindow.configure(bg = "#e6eded")

#Create Widgets


passLabel = Label(mainWindow, text = "PASSWORD", font = "roman 14 bold")
passLabel.grid(row=0, column=0)

showButton = Button(mainWindow, text="show/hide", command = lambda: showHide())
showButton.grid(row=1, column=0)

passEntry = Entry(mainWindow)
passEntry.grid(row=2, column=0)

sumbitButton = Button(mainWindow, text = "Submit", command = lambda: submit())
sumbitButton.grid(row=1, column=1)

successLabel = Label(mainWindow, text = "")
successLabel.grid(row=2, column=1)

#Display Label
mainWindow.mainloop()