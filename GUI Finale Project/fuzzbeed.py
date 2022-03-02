from tkinter import *
import random

#Var

page = 0
sixCon = False
S2e1 = ""
S2e2a = ""
S2e2b = ""
S2e3 = ""
S2e4a = ""
S2e4b = ""
S2e5 = ""
S2e6 = ""
S2e7 = ""
S2e8 = ""
S2e9 = ""
S2e10 = ""
S2e11 = ""
S2e12 = ""
S2e13 = ""
S2e14 = ""
S2e15 = ""
S3e16 = ""
S3e17 = ""
S3e18 = ""
S3e19 = ""
S3e20 = ""
S3e21a = ""
S3e21b = ""
manCon = 0
conCon = 0
cloneCon = 0
kojCon = 0
nameCat = 0
lickableScore = 0


#Functions

def roll1():
    manCon = random.randrange(1,5)
    
    S4Chap1Button.destroy()
def roll2():
    conCon
    S4Chap2Button.destroy()
def roll3():
    cloneCon
    S4Chap3Button.destroy()
def roll4():
    kojCon
    S4Chap4Button.destroy()

def startQuiz():
    openLabel.destroy()
    startButton.destroy()
    S2HeadLabel.grid(row = 0, column = 1)
    S2DesLabel.grid(row = 1, column = 1)
    S2Chap1Label.grid(row = 2, column = 1)
    S2Chap2aLabel.grid(row = 3, column = 1)
    S2Chap2bLabel.grid(row = 4, column = 1)
    S2Chap3Label.grid(row = 5, column = 1)
    S2Chap4aLabel.grid(row = 6, column = 1)
    S2Chap4bLabel.grid(row = 7, column = 1)
    S2Chap5Label.grid(row = 8, column = 1)
    S2Chap6Label.grid(row = 9, column = 1)
    S2Chap7Label.grid(row = 10, column = 1)
    S2Chap8Label.grid(row = 11, column = 1)
    S2Chap9Label.grid(row = 12, column = 1)
    S2Chap10Label.grid(row = 13, column = 1)
    S2Chap11Label.grid(row = 14, column = 1)
    S2Chap12Label.grid(row = 15, column = 1)
    S2Chap13Label.grid(row = 16, column = 1)
    S2Chap14Label.grid(row = 17, column = 1)
    S2Chap15Label.grid(row = 18, column = 1)
    continueButton.grid(row = 19, column = 2)

    S2Chap1Entry.grid(row = 2, column = 2)
    S2Chap2aEntry.grid(row = 3, column = 2)
    S2Chap2bEntry.grid(row = 4, column = 2)
    S2Chap3Entry .grid(row = 5, column = 2)
    S2Chap4aEntry.grid(row = 6, column = 2)
    S2Chap4bEntry.grid(row = 7, column = 2)
    S2Chap5Entry.grid(row = 8, column = 2)
    S2Chap6Entry.grid(row = 9, column = 2)
    S2Chap7Entry.grid(row = 10, column = 2)
    S2Chap8Entry.grid(row = 11, column = 2)
    S2Chap9Entry.grid(row = 12, column = 2)
    S2Chap10Entry.grid(row = 13, column = 2)
    S2Chap11Entry.grid(row = 14, column = 2)
    S2Chap12Entry.grid(row = 15, column = 2)
    S2Chap13Entry.grid(row = 16, column = 2)
    S2Chap14Entry.grid(row = 17, column = 2)
    S2Chap15Entry.grid(row = 18, column = 2)

def move1():
    S2HeadLabel.destroy()
    S2DesLabel.destroy()
    S2Chap1Label.destroy()
    S2Chap2aLabel.destroy()
    S2Chap2bLabel.destroy()
    S2Chap3Label.destroy()
    S2Chap4aLabel.destroy()
    S2Chap4bLabel.destroy()
    S2Chap5Label.destroy()
    S2Chap6Label.destroy()
    S2Chap7Label.destroy()
    S2Chap8Label.destroy()
    S2Chap9Label.destroy()
    S2Chap10Label.destroy()
    S2Chap11Label.destroy()
    S2Chap12Label.destroy()
    S2Chap13Label.destroy()
    S2Chap14Label.destroy()
    S2Chap15Label.destroy()
    continueButton.destroy()
    S2e1 = S2Chap1Entry.get()
    S2e2a = S2Chap2aEntry.get()
    S2e2b = S2Chap2bEntry.get()
    S2e3 = S2Chap3Entry.get()
    S2e4a = S2Chap4aEntry.get()
    S2e4b = S2Chap4bEntry.get()
    S2e5 = S2Chap5Entry.get()
    S2e6 = S2Chap6Entry.get()
    S2e7 = S2Chap7Entry.get()
    S2e8 = S2Chap8Entry.get()
    S2e9 = S2Chap9Entry.get()
    S2e10 = S2Chap10Entry.get()
    S2e11 = S2Chap11Entry.get()
    S2e12 = S2Chap12Entry.get()
    S2e13 = S2Chap13Entry.get()
    S2e14 = S2Chap14Entry.get()
    S2e15 = S2Chap15Entry.get()
    S2Chap1Entry.destroy()
    S2Chap2aEntry.destroy()
    S2Chap2bEntry.destroy()
    S2Chap3Entry.destroy()
    S2Chap4aEntry.destroy()
    S2Chap4bEntry.destroy()
    S2Chap5Entry.destroy()
    S2Chap6Entry.destroy()
    S2Chap7Entry.destroy()
    S2Chap8Entry.destroy()
    S2Chap9Entry.destroy()
    S2Chap10Entry.destroy()
    S2Chap11Entry.destroy()
    S2Chap12Entry.destroy()
    S2Chap13Entry.destroy()
    S2Chap14Entry.destroy()
    S2Chap15Entry.destroy()
    S3HeadLabel.grid(row = 0, column = 1)
    S3DesLabel.grid(row = 1, column = 1)
    S3Chap16Label.grid(row = 2, column = 1)
    S3Chap17Label.grid(row = 3, column = 1)
    S3Chap18Label.grid(row = 4, column = 1)
    S3Chap19Label.grid(row = 5, column = 1)
    S3Chap20Label.grid(row = 6, column = 1)
    S3Chap21aLabel.grid(row = 7, column = 1)
    S3Chap21bLabel.grid(row = 8, column = 1)
    S3Chap16Entry.grid(row = 2, column = 2)
    S3Chap17Entry.grid(row = 3, column = 2)
    S3Chap18Entry.grid(row = 4, column = 2)
    S3Chap19Entry.grid(row = 5, column = 2)
    S3Chap20Entry.grid(row = 6, column = 2)
    S3Chap21aEntry.grid(row = 7, column = 2)
    S3Chap21bEntry.grid(row = 8, column = 2)
    nextButton.grid(row = 9, column = 2)

def move2():
    S3HeadLabel.destroy()
    S3DesLabel.destroy()
    S3Chap16Label.destroy()
    S3Chap17Label.destroy()
    S3Chap18Label.destroy()
    S3Chap19Label.destroy()
    S3Chap20Label.destroy()
    S3Chap21aLabel.destroy()
    S3Chap21bLabel.destroy()
    S3Chap16Entry.destroy()
    S3Chap17Entry.destroy()
    S3Chap18Entry.destroy()
    S3Chap19Entry.destroy()
    S3Chap20Entry.destroy()
    S3Chap21aEntry.destroy()
    S3Chap21bEntry.destroy()
    nextButton.destroy()
    S4HeadLabel.grid(row =0 ,column = 1)
    S4DesLabel.grid(row =1 ,column = 1)
    S4Chap1Label.grid(row =2 ,column = 1)
    S4Chap2Label.grid(row =4 ,column = 1)
    S4Chap3Label.grid(row =6 ,column = 1)
    S4Chap4Label.grid(row =8 ,column = 1)
    S4Chap1Button.grid(row = 3, column =1)
    S4Chap2Button.grid(row = 5, column =1)
    S4Chap3Button.grid(row = 7, column =1)
    S4Chap4Button.grid(row = 9, column =1)


#Window Setup
mainWindow = Tk()
mainWindow.geometry("1200x500")
mainWindow.title("Fuzzbeed")
#Widgets

#StartUp
openLabel = Label(mainWindow, text = "Welcome!\nHave you ever wanted to know what your name would be if you were in one of Hideo Kojima's popular games such as Death Stranding or Metal Gear Solid? \nWell, now you can!")
openLabel.grid(row = 0, column = 0)

startButton = Button(mainWindow, text = "Start Quiz", command = lambda: startQuiz())
startButton.grid(row = 1, column = 0)

#Quiz
           ##Section 1 (Optional)
#       S1HeadLabel = Label(mainWindow, text = "Section 1: Determining How Many Names You Have")
#       S1HeadLabel.grid(row = 0, column = 0)
#       
#       S1DesChap1Label = Label(mainWindow, text = "Kojima often creates characters that have many alternate names, so we must first figure out how many names you will have.")

    #Section 2
S2HeadLabel = Label(mainWindow, text = "Section 2: Personal Information", font ="Roman 14")

S2DesLabel = Label(mainWindow, text = "Kojima’s characters have names that are directly related to their own character traits. This information will make sure your name fits your personality.", font = "Roman 10")

S2Chap1Label = Label(mainWindow, text = "What is your full name?")
S2Chap2aLabel = Label(mainWindow, text = "What do you do at your occupation?")
S2Chap2bLabel = Label(mainWindow, text = "Condense the verb in your answer into a single -er noun. (e.g. if you are a sheep farmer, your answer will be “farmer”)")
S2Chap3Label = Label(mainWindow, text = "What was your first pet’s specific species/breed? If you never had a pet, please answer with an animal you wish you owned.")
S2Chap4aLabel = Label(mainWindow, text = "What’s your most embarrassing childhood memory? Be specific and use full sentences.")
S2Chap4bLabel = Label(mainWindow, text = "Condense this story into two words.")
S2Chap5Label = Label(mainWindow, text = "What is the object you’d least like to be stabbed by?")
S2Chap6Label = Label(mainWindow, text = "What is something you are good at? (Verb ending in -ing)")
S2Chap7Label = Label(mainWindow, text = "How many carrots do you believe you could eat in one sitting, if someone, like, forced you to eat as many carrots as possible?")
S2Chap8Label = Label(mainWindow, text = "What is your greatest intangible fear? (e.g. death, loneliness, fear itself)")
S2Chap9Label = Label(mainWindow, text = "What is your greatest tangible fear? (e.g. horses)")
S2Chap10Label = Label(mainWindow, text = "What is the last thing you did before starting this worksheet?")
S2Chap11Label = Label(mainWindow, text = "What condition is your body currently in? (single word answer)")
S2Chap12Label = Label(mainWindow, text = "Favorite state of matter?")
S2Chap13Label = Label(mainWindow, text = "A word your name kind of sounds like? (e.g. Brian -> Brain)")
S2Chap14Label = Label(mainWindow, text = "What is your Zodiac sign?")
S2Chap15Label = Label(mainWindow, text = "If you had to define your personality in one word, what would it be?")

S2Chap1Entry = Entry(mainWindow,)
S2Chap2aEntry = Entry(mainWindow,)
S2Chap2bEntry = Entry(mainWindow,)
S2Chap3Entry = Entry(mainWindow,)
S2Chap4aEntry = Entry(mainWindow,)
S2Chap4bEntry = Entry(mainWindow,)
S2Chap5Entry = Entry(mainWindow,)
S2Chap6Entry = Entry(mainWindow,)
S2Chap7Entry = Entry(mainWindow,)
S2Chap8Entry = Entry(mainWindow,)
S2Chap9Entry = Entry(mainWindow,)
S2Chap10Entry = Entry(mainWindow,)
S2Chap11Entry = Entry(mainWindow,)
S2Chap12Entry = Entry(mainWindow,)
S2Chap13Entry = Entry(mainWindow,)
S2Chap14Entry = Entry(mainWindow,)
S2Chap15Entry = Entry(mainWindow,)

continueButton = Button(mainWindow, text = "Continue", command = lambda: move1())

    #Section 3
S3HeadLabel = Label(mainWindow, text = "Section 3: Kojima Information", font ="Roman 15")

S3DesLabel = Label(mainWindow, text = "Kojima character names reflect his own idiosyncrasies. He can’t help himself.", font ="Roman 16")

S3Chap16Label = Label(mainWindow, text = "Who is your favorite film character? (NOTE: must be played by Kurt Russell)")
S3Chap17Label = Label(mainWindow, text = "What is the last word of the title of your favorite Kubrick film?")
S3Chap18Label = Label(mainWindow, text = "What is the first word in the title of your favorite Joy Division album?")
S3Chap19Label = Label(mainWindow, text = "What is a scientific term you picked up from listening to NPR once? (If you have not listened to NPR, use a scientific term you don't know the meaning of)")
S3Chap20Label = Label(mainWindow, text = "What is a piece of military hardware you think looks cool even though waris bad?")
S3Chap21aLabel = Label(mainWindow, text = "What is something you’d enjoy watching Mads Mikkelsen do?")
S3Chap21bLabel = Label(mainWindow, text = "Please condense into one word.")

S3Chap16Entry = Entry(mainWindow)
S3Chap17Entry = Entry(mainWindow)
S3Chap18Entry = Entry(mainWindow)
S3Chap19Entry = Entry(mainWindow)
S3Chap20Entry = Entry(mainWindow)
S3Chap21aEntry = Entry(mainWindow)
S3Chap21bEntry = Entry(mainWindow)

nextButton = Button(mainWindow, text = "Continue", command = lambda: move2())
    #Section 4
S4HeadLabel = Label(mainWindow, text = "Section 4: Determining Your Name Conditions", font ="Roman 14")
S4DesLabel = Label(mainWindow, text = "Sometimes, a character will have a plot-based condition that affects their name. You, too, might have a condition that affects your name. Conditions can stack, so please make note of how many your name has.", font = "Roman 10")

S4Chap1Label = Label(mainWindow, text = "THE -MAN CONDITION: Click below to determine whether you have this condition (1/4 chance of getting)")
S4Chap1Button = Button(mainWindow, text = "Roll", command = lambda: roll1())
S4Chap2Label = Label(mainWindow, text = "THE CONDITION CONDITION: Click below to determine if you have this condition (3/8 chance of getting)")
S4Chap2Button = Button(mainWindow, text = "Roll", command = lambda: roll2())
S4Chap3Label = Label(mainWindow, text = "THE CLONE CONDITION: Click below to determine if you have this condition (1/12 chance of getting)")
S4Chap3Button = Button(mainWindow, text = "Roll", command = lambda: roll3())
S4Chap4Label = Label(mainWindow, text = "--[OPTIONAL]--THE KOJIMA CONDITION: Click below to determine if you have this condition (1/100 chance of getting)")
S4Chap4Button = Button(mainWindow, text = "Roll", command = lambda: roll4())

    #Section 5
S5HeadLabel = Label(mainWindow, text = "Section 5: Determining Your Name Category", font ="Roman 14")
S5DesLabel = Label(mainWindow, text = "Kojima names fall into a finite number of categories. This section will determine the category in which your name belongs. NOTE:If you have a name + 6 alternate names, you will do this section once to find your true name, and then you will have an alternate name in every other category.", font = "Roman 9")
S5Chap1Label = Label(mainWindow, text = "Click below to determine your name category. Once you have figured out your name category, you can skip ahead to the section that outlines the rules of your name:")

#Results


mainWindow.mainloop()