from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox

def buttons(controller, root):
    fontSettings = font.Font(size = 12)

    # New Litter
    newLButton = Button(root, text="New Litter", command=lambda: newLitterMenu(controller, root))
    newLButton['font'] = fontSettings
    newLButton.grid(row = 0, column = 0, pady = 10, padx = 10, sticky=W, columnspan=2)

    # Clear Litters
    newCButton = Button(root, text="Clear All Litters", command=lambda: controller.clearLitters())
    newCButton['font'] = fontSettings
    newCButton.grid(row = 0, column = 1, pady = 10, padx = 10, sticky=W, columnspan=2)

def bunnyInfo(controller, root):
    # Label at the top
    controller.bunnyInfo["NumberLabel"] = Label(root, text="Bunny #", font=(18)).grid(row = 0, column = 7, pady = 20, padx = 20)

    # Picture
    bunnyPic = PhotoImage(file='placeholder.gif')
    controller.bunnyInfo["BunnyPicLabel"] = Label(root, image=bunnyPic).grid(row = 1, column = 7, pady = 20, padx = 30)
    controller.bunnyInfo["BunnyPicture"] = bunnyPic

    # Info below picture
    controller.bunnyInfo["InfoLabel"] = Label(root, text="Sex:\nAlbino:\nColor:\nPattern:\nTremor:", font=(14)).grid(row=2, column = 7, padx = 20, pady = 20)

# TODO: before this pops up, calculate all males and females or something to pull into dropdown?
def newLitterMenu(controller, root):
    fontSettings = font.Font(size = 12)

    litterMenu = Toplevel(root)
    litterMenu.title("New Litter Menu")

    Label(litterMenu, text="Mother").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    motherBox = Combobox(litterMenu, values=controller.motherTable, state='readonly')
    motherBox.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    Label(litterMenu, text="Father").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    fatherBox = Combobox(litterMenu, values=controller.fatherTable, state='readonly')
    fatherBox.grid(row=3, column=0, padx=10, pady=10, sticky=W)

    Label(litterMenu, text="Number of Offspring").grid(row=4, column=0, padx=10, pady=10, sticky=W)
    offspringNumBox = Combobox(litterMenu, values=controller.offspringTable, state='readonly')
    #offspringNumBox = Entry(litterMenu)
    offspringNumBox.grid(row=5, column=0, padx=10, pady=10, sticky=W)

    # TODO: need some edge case checking on the integer input for offspringNumBox.
    okButton = Button(litterMenu, text="Okay", command=lambda: controller.generateNewLitter(motherBox.get(), fatherBox.get(), offspringNumBox.get()))
    okButton['font'] = fontSettings
    okButton.grid(row=6, column=0, padx=10, pady=10, sticky=W)

def newBunnyMenu(controller, root):
    fontSettings = font.Font(size = 12)

    bunnyMenu = Toplevel(root)
    bunnyMenu.title("New Bunny Menu")

    # Albino
    albinoVar = StringVar(value="Yes")
    Label(bunnyMenu, text="Albino").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    aY = Radiobutton(bunnyMenu, text="Yes", variable=albinoVar, value="Yes")
    aY.grid(row=1, column=0, padx=5, pady=5)
    aN = Radiobutton(bunnyMenu, text="No", variable=albinoVar, value="No")
    aN.grid(row=1, column=1, padx=5, pady=5)

    # Color
    colorVar = StringVar(value="Black")
    Label(bunnyMenu, text="Color").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    cB = Radiobutton(bunnyMenu, text="Black", variable=colorVar, value="Black")
    cB.grid(row=3, column=0, padx=5, pady=5)

    cG = Radiobutton(bunnyMenu, text="Grey", variable=colorVar, value="Grey")
    cG.grid(row=3, column=1, padx=5, pady=5)

    cC = Radiobutton(bunnyMenu, text="Chocolate", variable=colorVar, value="Chocolate")
    cC.grid(row=3, column=2, padx=5, pady=5)

    cL = Radiobutton(bunnyMenu, text="Lilac", variable=colorVar, value="Lilac")
    cL.grid(row=3, column=3, padx=5, pady=5)

    # Spotting
    spottingVar = StringVar(value="Broken")
    Label(bunnyMenu, text="Spotting").grid(row=4, column=0, padx=10, pady=10, sticky=W)
    sB = Radiobutton(bunnyMenu, text="Broken", variable=spottingVar, value="Broken")
    sB.grid(row=5, column=0, padx=5, pady=5)

    sC = Radiobutton(bunnyMenu, text="Charlie", variable=spottingVar, value="Charlie")
    sC.grid(row=5, column=1, padx=5, pady=5)

    sS = Radiobutton(bunnyMenu, text="Solid", variable=spottingVar, value="Solid")
    sS.grid(row=5, column=2, padx=5, pady=5)

    # Tremor
    tremorVar = StringVar(value="Yes")
    Label(bunnyMenu, text="Tremor").grid(row=6, column=0, padx=10, pady=10, sticky=W)
    aY = Radiobutton(bunnyMenu, text="Yes", variable=tremorVar, value="Yes")
    aY.grid(row=7, column=0, padx=5, pady=5)
    aN = Radiobutton(bunnyMenu, text="No", variable=tremorVar, value="No")
    aN.grid(row=7, column=1, padx=5, pady=5)
    
    okButton = Button(bunnyMenu, text="Okay", command=lambda: testPrint(albinoVar.get(), colorVar.get(), spottingVar.get(), tremorVar.get()))
    okButton['font'] = fontSettings
    okButton.grid(row=8, column=0, padx=10, pady=10, sticky=W)

def testPrint(albinoVar, colorVar, spottingVar, tremorVar):
    print(albinoVar, colorVar, spottingVar, tremorVar)