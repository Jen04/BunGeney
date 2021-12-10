from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox
from tkinter import messagebox

def newLitterMenu(controller, root, pot_mothers, pot_fathers):
    # Sets start of dropdowns so "New" is always an option
    mothers = ["New"] + pot_mothers
    fathers = ["New"] + pot_fathers
    if len(pot_mothers) == 0:
        pot_mothers = "New"
    if len(pot_fathers) == 0:
        pot_fathers = "New"

    fontSettings = font.Font(size = 12)

    litterMenu = Toplevel(root)
    litterMenu.title("New Litter Menu")
    litterMenu.resizable(False, False)
    litterMenu.focus_set()
    litterMenu.grab_set()

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

# Called by newLitterMenu to determine where to send collected data
def checkInput(controller, root, litterMenu, motherNum, fatherNum, offspringNum):
    # Make sure it's an int
    try: 
        strToNum = int(offspringNum)
    except ValueError:
        messagebox.showerror(title="Invalid Input", message="Please enter a number for number of offspring.")
        return
    
    # Make sure it's positive
    if strToNum < 1:
        messagebox.showerror(title="Invalid Input", message="Please enter a valid number of offspring.")
        return

    # Make sure offspringNum isn't larger than 100
    if strToNum > 100:
        messagebox.showerror(title="Invalid Input", message="Please choose a number less than or equal to 100 for number of offspring.")
        return

    # Choose with menu to use based on input, and create them
    if motherNum == "New" and fatherNum == "New":
        litterMenu.destroy()
        newParentsMenu(controller, root, offspringNum)
    elif motherNum == "New":
        litterMenu.destroy()
        newBunnyMenu(controller, controller.root, "Mother", motherNum, fatherNum, offspringNum)
    elif fatherNum == "New":
        litterMenu.destroy()
        newBunnyMenu(controller, controller.root, "Father", motherNum, fatherNum, offspringNum)
    else:
        controller.setExistingBunnies(litterMenu, motherNum, fatherNum, offspringNum)

def newParentsMenu(controller, root, offspringNum):
    parentsMenu = Toplevel(root)
    parentsMenu.resizable(False, False)
    parentsMenu.title("New Parents")
    parentsMenu.focus_set()
    parentsMenu.grab_set()

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

    okButton = Button(parentsMenu, text="Okay", command=lambda: controller.setFirstGeneration(parentsMenu, mAlbinoBox.get(), mColorBox.get(), mSpottingBox.get(), mTremorBox.get(), fAlbinoBox.get(), fColorBox.get(), fSpottingBox.get(), fTremorBox.get(), offspringNum))
    okButton.grid(row=9, column=0, padx=10, pady=10, sticky=W)

def newBunnyMenu(controller, root, parentType, motherNum, fatherNum, offspringNum):
    nBunnyMenu = Toplevel(root)
    nBunnyMenu.resizable(False, False)
    nBunnyMenu.title("New " + parentType)
    nBunnyMenu.focus_set()
    nBunnyMenu.grab_set()

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
    
    okButton = Button(nBunnyMenu, text="Okay", command=lambda: controller.setNewParentInfo(nBunnyMenu, albinoBox.get(), colorBox.get(), spottingBox.get(), tremorBox.get(), parentType, motherNum, fatherNum, offspringNum))
    okButton.grid(row=9, column=0, padx=10, pady=10, sticky=W)

