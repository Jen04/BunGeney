from tkinter import *
import tkinter.font as font


def buttons(controller, view, root):
    fontSettings = font.Font(size = 16)

    # New Litter
    newLButton = Button(root, text="New Litter", command=lambda: controller.newLitter())
    newLButton['font'] = fontSettings
    newLButton.grid(row = 0, column = 0, pady = 10, padx = 10)

    # Clear Litters
    newCButton = Button(root, text="Clear All Litters", command=lambda: controller.clearLitters())
    newCButton['font'] = fontSettings
    newCButton.grid(row = 0, column = 1, pady = 10, padx = 10)

def bunnyInfo(controller, root):
    # Label at the top
    bunnyLabel = Label(root, text="Bunny #", font=(16))
    bunnyLabel.grid(row = 0, column=3, pady = 10, padx = 10)
    controller.bunnyInfo["NumberLabel"] = bunnyLabel

    # Picture
    bunnyPic = PhotoImage(file='placeholder.gif')
    bunnyPicLbl = Label(root, image=bunnyPic)
    bunnyPicLbl.grid(row = 1, column = 3, pady = 10, padx = 10)
    controller.bunnyInfo["BunnyPicLabel"] = bunnyPicLbl
    controller.bunnyInfo["BunnyPicture"] = bunnyPic

    # Info below picture
    



