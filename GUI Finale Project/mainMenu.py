from tkinter import *
import PhotoGal
import rectangleCalc
#import fuzzbeed
#import trivia
import aboutPage
import randNumGen

def init():

    def aboutCom():
        aboutPage.init()
    def photoCom():
        photoGal.init()
    def rectangleCom():
        rectangleCalc.init()
    def randNumCom():
        randNumGen.init()
   def triviaCom():
       trivia.init()

        

    mainWindow = Tk()
    mainWindow.geometry("550x100")
    mainWindow.title("The Menu At Which You Have Access To The Rest Of The Programs")

    photoButton = Button(mainWindow, text = "Photo Gallery", command = lambda:photoCom())
    photoButton.grid(row = 1, column = 0)
    aboutButton = Button(mainWindow, text = "About Page", command = lambda:aboutCom())
    aboutButton.grid(row = 0, column = 0)
    rectangleButton = Button(mainWindow, text = "Area Calculator", command = lambda:rectangleCom())
    rectangleButton.grid(row = 2, column = 0)
    randomNumButton = Button(mainWindow, text = "Random Number Generator", command = lambda:randNumCom())
    randomNumButton.grid(row = 0, column = 1)
    triviaButton = Button(mainWindow, text = "Trivia", command = lambda:triviaCom())
    triviaButton.grid(row = 1, column = 1)


    mainWindow.mainloop()