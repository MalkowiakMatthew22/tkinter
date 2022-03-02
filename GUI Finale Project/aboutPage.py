from tkinter import *


def init():
    mainWindow = Tk()
    mainWindow.geometry("700x200")
    mainWindow.title("'About Page?' What About Page? Did Something Happen to Page?")
    Label1 = Label(mainWindow, text = "Hello, I'm Matthew", font = "Roman 20 bold")
    Label1.grid(row = 0, column = 0)
    Label2 = Label(mainWindow, text = "I made the program that you are currently using in the year 2022, I know, it was a while ago, and yes this was still bad for today's standard. Not only did I make this in my intro to programing class, but I still don't have a great grasp of all of the stuff we went over (which is on me). This program and all of it's functions probably can't be over 600 lines of code on Python, uncondensed of course. The funniest part of all of this is the fact that I still don't know how to use Github. I was gone the one day we talked about how to use it and set it up and never got an understanding of it even with the recordings, luckily I don't think I'll be needing to know programming in my future.", font = "Roman 12", wraplength = 700)
    Label2.grid(row = 1, column = 0)
    mainWindow.mainloop()