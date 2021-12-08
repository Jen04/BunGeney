from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox
from tkinter import messagebox
import Main

def buttons(controller, root):
    fontSettings = font.Font(size = 12)

    # New Litter
    # TODO: create conditional to choose what menus pop up when this button is clicked. If there is no existing litter, it needs to prompt user for mother and father creation
    controller.newLButton = Button(root, text="New Litter", command=lambda: newLitterMenu(controller, root, Main.pot_mothers(), Main.pot_fathers()))
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
# TODO: REMOVE X otherwise things break 
def newLitterMenu(controller, root, pot_mothers, pot_fathers):
    mothers = ["New"] + pot_mothers
    fathers = ["New"] + pot_fathers
    if len(pot_mothers) == 0:
        pot_mothers = "New"
    if len(pot_fathers) == 0:
        pot_fathers = "New"

    controller.newLButton.configure(state=DISABLED)
    fontSettings = font.Font(size = 12)

    litterMenu = Toplevel(root)
    litterMenu.title("New Litter Menu")
    litterMenu.resizable(False, False)

    Label(litterMenu, text="Mother").grid(row=0, column=0, padx=10, pady=10, sticky=W)
    motherBox = Combobox(litterMenu, values=mothers, state='readonly')
    motherBox.grid(row=1, column=0, padx=30, pady=10, sticky=W)
    motherBox.current(0)

    Label(litterMenu, text="Father").grid(row=2, column=0, padx=10, pady=10, sticky=W)
    fatherBox = Combobox(litterMenu, values=fathers, state='readonly')
    fatherBox.grid(row=3, column=0, padx=30, pady=10, sticky=W)
    fatherBox.current(0)

    Label(litterMenu, text="Number of Offspring").grid(row=4, column=0, padx=10, pady=10, sticky=W)
    offspringNumBox = Entry(litterMenu)
    offspringNumBox.grid(row=5, column=0, padx=30, pady=10, sticky=W, columnspan=1)

    okButton = Button(litterMenu, text="Okay", command=lambda: checkInput(controller, root, litterMenu, motherBox.get(), fatherBox.get(), offspringNumBox.get()))
    okButton['font'] = fontSettings
    okButton.grid(row=6, column=0, padx=30, pady=10, sticky=W)

def checkInput(controller, root, litterMenu, motherNum, fatherNum, offspringNum):

    # Is it an int?
    try: 
        strToNum = int(offspringNum)
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

    controller.currentMother = motherNum
    controller.currentFather = fatherNum
    controller.offspringNum = offspringNum

    if motherNum == "New" and fatherNum == "New":
        litterMenu.destroy()
        newParentsMenu(controller, root)
    elif motherNum == "New":
        litterMenu.destroy()
        newBunnyMenu(controller, controller.root, "Mother")
    elif fatherNum == "New":
        litterMenu.destroy()
        newBunnyMenu(controller, controller.root, "Father")
    else:
        controller.setExistingBunnies(litterMenu)

def newParentsMenu(controller, root):
    # Father
    controller.newLButton.configure(state=DISABLED)

    fontSettings = font.Font(size = 12)

    parentsMenu = Toplevel(root)
    parentsMenu.resizable(False, False)
    parentsMenu.title("New Parents")

    # ------------------ ( New Father ) ------------------ 
    Label(parentsMenu, text="New Father").grid(row=0, column=0, padx=10, pady=10, sticky=W)

    # Albino
    Label(parentsMenu, text="Albino").grid(row=1, column=0, padx=10, pady=10, sticky=W)
    fAlbinoBox = Combobox(parentsMenu, values=controller.dropDownList[0], state='readonly')
    fAlbinoBox.grid(row=2, column=0, padx=30, pady=10, sticky=W)
    fAlbinoBox.current(0)

    # Color
    Label(parentsMenu, text="Color").grid(row=3, column=0, padx=10, pady=10, sticky=W)
    fColorBox = Combobox(parentsMenu, values=controller.dropDownList[1], state='readonly')
    fColorBox.grid(row=4, column=0, padx=30, pady=10, sticky=W)
    fColorBox.current(0)

    # Spotting
    Label(parentsMenu, text="Spotting").grid(row=5, column=0, padx=10, pady=10, sticky=W)
    fSpottingBox = Combobox(parentsMenu, values=controller.dropDownList[2], state='readonly')
    fSpottingBox.grid(row=6, column=0, padx=30, pady=10, sticky=W)
    fSpottingBox.current(0)

    # Tremor
    Label(parentsMenu, text="Tremor").grid(row=7, column=0, padx=10, pady=10, sticky=W)
    fTremorBox = Combobox(parentsMenu, values=controller.dropDownList[0], state='readonly')
    fTremorBox.grid(row=8, column=0, padx=30, pady=10, sticky=W)
    fTremorBox.current(0)

    # ------------------ ( New Mother ) ------------------ 
    Label(parentsMenu, text="New Mother").grid(row=0, column=3, padx=10, pady=10, sticky=W)

    # Albino
    Label(parentsMenu, text="Albino").grid(row=1, column=3, padx=10, pady=10, sticky=W)
    mAlbinoBox = Combobox(parentsMenu, values=controller.dropDownList[0], state='readonly')
    mAlbinoBox.grid(row=2, column=3, padx=30, pady=10, sticky=W)
    mAlbinoBox.current(0)

    # Color
    Label(parentsMenu, text="Color").grid(row=3, column=3, padx=10, pady=10, sticky=W)
    mColorBox = Combobox(parentsMenu, values=controller.dropDownList[1], state='readonly')
    mColorBox.grid(row=4, column=3, padx=30, pady=10, sticky=W)
    mColorBox.current(0)

    # Spotting
    Label(parentsMenu, text="Spotting").grid(row=5, column=3, padx=10, pady=10, sticky=W)
    mSpottingBox = Combobox(parentsMenu, values=controller.dropDownList[2], state='readonly')
    mSpottingBox.grid(row=6, column=3, padx=30, pady=10, sticky=W)
    mSpottingBox.current(0)

    # Tremor
    Label(parentsMenu, text="Tremor").grid(row=7, column=3, padx=10, pady=10, sticky=W)
    mTremorBox = Combobox(parentsMenu, values=controller.dropDownList[0], state='readonly')
    mTremorBox.grid(row=8, column=3, padx=30, pady=10, sticky=W)
    mTremorBox.current(0)

    # msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
    okButton = Button(parentsMenu, text="Okay", command=lambda: controller.setFirstGeneration(parentsMenu, mAlbinoBox.get(), mColorBox.get(), mSpottingBox.get(), mTremorBox.get(), fAlbinoBox.get(), fColorBox.get(), fSpottingBox.get(), fTremorBox.get()))
    okButton.grid(row=9, column=0, padx=10, pady=10, sticky=W)

def newRadioButton(controller, menu, name, txt, var, val, r, c):
    controller.rbDict[name] = Radiobutton(menu, text=txt, variable=var, value=val)
    controller.rbDict[name].grid(row=r, column=c, padx=5, pady=5, sticky=W)

def newBunnyMenu(controller, root, parentType):
    controller.newLButton.configure(state=DISABLED)

    fontSettings = font.Font(size = 12)

    nBunnyMenu = Toplevel(root)
    nBunnyMenu.resizable(False, False)
    nBunnyMenu.title("New " + parentType)

    Label(nBunnyMenu, text="New " + parentType).grid(row=0, column=0, padx=10, pady=10, sticky=W)

    # Albino
    Label(nBunnyMenu, text="Albino").grid(row=1, column=0, padx=10, pady=10, sticky=W)
    albinoBox = Combobox(nBunnyMenu, values=controller.dropDownList[0], state='readonly')
    albinoBox.grid(row=2, column=0, padx=30, pady=10, sticky=W)
    albinoBox.current(0)

    # Color
    Label(nBunnyMenu, text="Color").grid(row=3, column=0, padx=10, pady=10, sticky=W)
    colorBox = Combobox(nBunnyMenu, values=controller.dropDownList[1], state='readonly')
    colorBox.grid(row=4, column=0, padx=30, pady=10, sticky=W)
    colorBox.current(0)

    # Spotting
    Label(nBunnyMenu, text="Spotting").grid(row=5, column=0, padx=10, pady=10, sticky=W)
    spottingBox = Combobox(nBunnyMenu, values=controller.dropDownList[2], state='readonly')
    spottingBox.grid(row=6, column=0, padx=30, pady=10, sticky=W)
    spottingBox.current(0)

    # Tremor
    Label(nBunnyMenu, text="Tremor").grid(row=7, column=0, padx=10, pady=10, sticky=W)
    tremorBox = Combobox(nBunnyMenu, values=controller.dropDownList[0], state='readonly')
    tremorBox.grid(row=8, column=0, padx=30, pady=10, sticky=W)
    tremorBox.current(0)
    
    okButton = Button(nBunnyMenu, text="Okay", command=lambda: controller.setNewParentInfo(nBunnyMenu, albinoBox.get(), colorBox.get(), spottingBox.get(), tremorBox.get(), parentType))
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