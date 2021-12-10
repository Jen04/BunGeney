from tkinter import *

# Controls the individual bunny data that displays on the right side of the window
class BunnyInfo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller
        self.bunnyInfo = {}
    
    def createFields(self):
        # Label at the top
        self.bunnyInfo["NumberLabel"] = Label(self.parent, text="Bunny #", font=(18))
        self.bunnyInfo["NumberLabel"].grid(row = 1, column = 14, pady = 20, padx = 20)

        # Picture
        bunnyPic = PhotoImage(file='Pictures/Default.png')
        self.bunnyInfo["BunnyPicLabel"] = Label(self.parent, image=bunnyPic)
        self.bunnyInfo["BunnyPicLabel"].grid(row = 2, column = 14, pady = 20, padx = 30)
        self.bunnyInfo["BunnyPicture"] = bunnyPic

        # Info below picture
        self.bunnyInfo["InfoLabel"] = Label(self.parent, text="Sex:\nAlbino:\nColor:\nPattern:\nTremor:", font=(14))
        self.bunnyInfo["InfoLabel"].grid(row=3, column = 14, padx = 20, pady = 20)

    def setDefaults(self):
        self.setNumberLbl("")
        self.setPic('Pictures/Default.png')
        self.setInfo("", "", "", "", "")

    def setNumberLbl(self, num):
        self.bunnyInfo["NumberLabel"].configure(text="Bunny # " + num)

    def setPic(self, f):
        bunnyPic = PhotoImage(file=f)
        self.bunnyInfo["BunnyPicLabel"].configure(image=bunnyPic)
        self.bunnyInfo["BunnyPicture"] = bunnyPic

    def setInfo(self, sex, albino, color, pattern, tremor):
        self.bunnyInfo["InfoLabel"].configure(text="Sex: "+ sex + "\nAlbino: " + albino + "\nColor: " + color + "\nPattern: " + pattern + "\nTremor: " + tremor)