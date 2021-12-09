from tkinter import *

class BunnyInfo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.bunnyInfo = {}
    
    def createFields(self):
        # Label at the top
        self.bunnyInfo["NumberLabel"] = Label(self.parent, text="Bunny #", font=(18))
        self.bunnyInfo["NumberLabel"].grid(row = 0, column = 7, pady = 20, padx = 20)

        # Picture
        bunnyPic = PhotoImage(file='placeholder.gif')
        self.bunnyInfo["BunnyPicLabel"] = Label(self.parent, image=bunnyPic)
        self.bunnyInfo["BunnyPicLabel"].grid(row = 1, column = 7, pady = 20, padx = 30)
        self.bunnyInfo["BunnyPicture"] = bunnyPic

        # Info below picture
        self.bunnyInfo["InfoLabel"] = Label(self.parent, text="Sex:\nAlbino:\nColor:\nPattern:\nTremor:", font=(14))
        self.bunnyInfo["InfoLabel"].grid(row=2, column = 7, padx = 20, pady = 20)

    def setNumberLbl(self, num):
        self.bunnyInfo["NumberLabel"].configure(text="Bunny # " + num)

    def setPic(self, f):
        # Picture
        bunnyPic = PhotoImage(file=f)
        self.bunnyInfo["BunnyPicLabel"].configure(image=bunnyPic)
        self.bunnyInfo["BunnyPicture"] = bunnyPic

    def setInfo(self, sex, albino, color, pattern, tremor):
        self.bunnyInfo["InfoLabel"].configure(text="Sex: "+ sex + "\nAlbino: " + albino + "\nColor: " + color + "\nPattern: " + pattern + "\nTremor: " + tremor)