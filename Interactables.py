from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox
from tkinter import messagebox

def buttons(controller, root):
    fontSettings = font.Font(size = 12)

    # New Litter
    # TODO: create conditional to choose what menus pop up when this button is clicked. If there is no existing litter, it needs to prompt user for mother and father creation
    controller.newLButton = Button(root, text="New Litter", command=lambda: controller.newParents())
    controller.newLButton['font'] = fontSettings
    controller.newLButton.grid(row = 0, column = 0, pady = 10, padx = 10, sticky=W, columnspan=2)

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
    controller.newLButton.configure(state=DISABLED)
    fontSettings = font.Font(size = 12)

    litterMenu = Toplevel(root)
    litterMenu.title("New Litter Menu")
    litterMenu.resizable(False, False)
    litterMenu.attributes('-topmost', 1)

    Label(litterMenu, text="Mother").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    motherBox = Combobox(litterMenu, values=controller.motherTable, state='readonly')
    motherBox.grid(row=1, column=0, padx=30, pady=10, sticky=W)
    motherBox.current(1)

    Label(litterMenu, text="Father").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    fatherBox = Combobox(litterMenu, values=controller.fatherTable, state='readonly')
    fatherBox.grid(row=3, column=0, padx=30, pady=10, sticky=W)
    fatherBox.current(1)

    Label(litterMenu, text="Number of Offspring").grid(row=4, column=0, padx=10, pady=10, sticky=W)
    offspringNumBox = Entry(litterMenu)
    offspringNumBox.grid(row=5, column=0, padx=30, pady=10, sticky=W, columnspan=1)

    okButton = Button(litterMenu, text="Okay", command=lambda: checkInput(controller, litterMenu, motherBox.get(), fatherBox.get(), offspringNumBox.get()))
    okButton['font'] = fontSettings
    okButton.grid(row=6, column=0, padx=30, pady=10, sticky=W)

def checkInput(controller, litterMenu, motherNum, fatherNum, offSpringNum):
    # Is it an int?
    try: 
        strToNum = int(offSpringNum)
    except ValueError:
        messagebox.showerror(title="Invalid Input", message="Please enter a number for number of offspring.")
        return
    
    # Is it positive?
    if strToNum < 1:
        messagebox.showerror(title="Invalid Input", message="Please enter a valid number of offspring.")
        return

    # Too many bunnies?
    if strToNum > 100:
        messagebox.showerror(title="Invalid Input", message="Please choose a number less than or equal to 100 for number of offspring.")
        return
    
    # Passed all checks, pass the info along
    controller.generateNewLitter(litterMenu, motherNum, fatherNum, offSpringNum)

# TODO: Infinite number of newlitters can pop up, probably same with the other one. Fix this somehow
def newBunnyMenu(controller, root, parentType):
    # TODO: DISABLE X ON WINDOW
    controller.newLButton.configure(state=DISABLED)

    fontSettings = font.Font(size = 12)

    bunnyMenu = Toplevel(root)
    bunnyMenu.resizable(False, False)
    bunnyMenu.attributes('-topmost', 1)

    bunnyMenu.title("New " + parentType + " Menu")
    Label(bunnyMenu, text="New " + parentType).grid(row=0, column=0, padx=10, pady=10, sticky=W)

    # Albino
    albinoVar = StringVar(value="No")
    Label(bunnyMenu, text="Albino").grid(row=1, column=0, padx=10, pady=10, sticky=W)
    aN = Radiobutton(bunnyMenu, text="No", variable=albinoVar, value="No", command=lambda: radiobuttonsOn(cB, cG, cC, cL, sB, sC, sS))
    aN.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    aY = Radiobutton(bunnyMenu, text="Yes", variable=albinoVar, value="Yes", command=lambda: radiobuttonsOff(cB, cG, cC, cL, sB, sC, sS))
    aY.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    # Color
    colorVar = StringVar(value="Black")
    Label(bunnyMenu, text="Color").grid(row=3, column=0, padx=10, pady=10, sticky=W)
    cB = Radiobutton(bunnyMenu, text="Black", variable=colorVar, value="Black")
    cB.grid(row=4, column=0, padx=5, pady=5, sticky=W)

    cG = Radiobutton(bunnyMenu, text="Grey", variable=colorVar, value="Grey")
    cG.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    cC = Radiobutton(bunnyMenu, text="Chocolate", variable=colorVar, value="Chocolate")
    cC.grid(row=4, column=2, padx=5, pady=5, sticky=W)

    cL = Radiobutton(bunnyMenu, text="Lilac", variable=colorVar, value="Lilac")
    cL.grid(row=4, column=3, padx=5, pady=5, sticky=W)

    # Spotting
    spottingVar = StringVar(value="Broken")
    Label(bunnyMenu, text="Spotting").grid(row=5, column=0, padx=10, pady=10, sticky=W)
    sB = Radiobutton(bunnyMenu, text="Broken", variable=spottingVar, value="Broken")
    sB.grid(row=6, column=0, padx=5, pady=5, sticky=W)

    sC = Radiobutton(bunnyMenu, text="Charlie", variable=spottingVar, value="Charlie")
    sC.grid(row=6, column=1, padx=5, pady=5, sticky=W)

    sS = Radiobutton(bunnyMenu, text="Solid", variable=spottingVar, value="Solid")
    sS.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    # Tremor
    tremorVar = StringVar(value="No")
    Label(bunnyMenu, text="Tremor").grid(row=7, column=0, padx=10, pady=10, sticky=W)
    tN = Radiobutton(bunnyMenu, text="No", variable=tremorVar, value="No")
    tN.grid(row=8, column=0, padx=5, pady=5, sticky=W)
    tY = Radiobutton(bunnyMenu, text="Yes", variable=tremorVar, value="Yes")
    tY.grid(row=8, column=1, padx=5, pady=5, sticky=W)
    
    okButton = Button(bunnyMenu, text="Okay", command=lambda: controller.setNewInfo(bunnyMenu, albinoVar.get(), colorVar.get(), spottingVar.get(), tremorVar.get(), parentType))
    okButton['font'] = fontSettings
    okButton.grid(row=9, column=0, padx=10, pady=10, sticky=W)

def radiobuttonsOn(cB, cG, cC, cL, sB, sC, sS):
    cB.configure(state=NORMAL)
    cG.configure(state=NORMAL)
    cC.configure(state=NORMAL)
    cL.configure(state=NORMAL)
    sB.configure(state=NORMAL)
    sC.configure(state=NORMAL)
    sS.configure(state=NORMAL)
def radiobuttonsOff(cB, cG, cC, cL, sB, sC, sS):
    cB.configure(state=DISABLED)
    cG.configure(state=DISABLED)
    cC.configure(state=DISABLED)
    cL.configure(state=DISABLED)
    sB.configure(state=DISABLED)
    sC.configure(state=DISABLED)
    sS.configure(state=DISABLED)

def testPrint(albinoVar, colorVar, spottingVar, tremorVar):
    print(albinoVar, colorVar, spottingVar, tremorVar)