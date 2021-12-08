import Interactables
import Main
from BunnyTable import BunnyTable
from TotalsTable import TotalsTable
from tkinter import *

class Controller:
    def __init__(self, view):
        #self.model = model
        self.view = view
        self.root = self.view.master

        # Stored inside: NumberLabel, BunnyPicLabel, BunnyPicture, InfoLabel. 
        # This info is changed when changeSelectedBunny is clicked.
        self.bunnyInfo = {}        
        # Row list used within Table.py. All row buttons are contained within this
        self.rowList = []
        # Dropdown options when selecting info for a new bunny
        self.dropDownList = [["No", "Yes"], ["Black", "Gray", "Chocolate", "Lilac"], ["Broken", "Charlie", "Solid"]]

        # This is used to change what the button does when clicked based on if a litter already exists
        self.newLButton = ""

        self.createButtons()
        self.createBunnyInfo()

        # Create bunny table
        self.table = BunnyTable(self.root, self)
        # Create totals table
        self.totalTable = TotalsTable(self.root, self)
        # TODO: Temporary list of values that needs to be replaced with mothers/fathers
        self.motherTable = ["New"]
        self.fatherTable = ["New"]

        # Used in bunny generation
        self.offspringNum = 0
        self.currentMother = ""
        self.currentFather = ""

        # Set column lables for bunny table, set initial values for totals table
        self.tableSetup()

    def tableSetup(self):
        self.table.addFirstRow()
        self.totalTable.setUpTable()
 
    # Creates some of the buttons on the GUI
    def createButtons(self):
        Interactables.buttons(self, self.root)

    # Creates the info to the right of the GUI that shows individual bunny info
    def createBunnyInfo(self):
        Interactables.bunnyInfo(self, self.root)

    # Adds the labels at the top of the table
    def newLitter(self):
        self.table.addFirstRow()

    # Clears litters from table
    # TODO: make sure this is clearing everything it should
    def clearLitters(self):
        self.table.deleteAllRows()
        self.tableSetup()
        self.currentMother = ""
        self.currentFather = ""
        self.offspringNum = 0
        self.motherTable = ["New"]
        self.fatherTable = ["New"]
        Main.clearValues()

    # Adds individual bunny to the table
    def addBunnyToTable(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        self.table.addNormalRow(bunNum, bunParents, sex, albino, color, pattern, tremor)

    # Activates after litterMenu is filled out and "okay" button is clicked.
    #TODO: HOOK UP WITH JOE'S STUFF.

    # mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
    def setNewParentInfo(self, menu, albino, color, spotting, tremor, parentType):
        # Check which parent is new, put zeroes for the other one or something
        menu.destroy()
        self.newLButton.configure(state=NORMAL)

        # mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
        if parentType == "Mother":
            Main.total(self, "new", self.currentFather, self.offspringNum, "Female", albino, color, spotting, tremor, 0, 0, 0, 0, 0)

        elif parentType == "Father":
            Main.total(self, self.currentMother, "new", self.offspringNum, 0, 0, 0, 0, 0, "Male", albino, color, spotting, tremor)
        else:
            print("Something went wrong.")

    def setExistingBunnies(self, litterMenu):
        litterMenu.destroy()
        Main.total(self, self.currentMother, self.currentFather, self.offspringNum, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Starting here ****
    def setFirstGeneration(self, menu, malbino, mcolor, mspotting, mtremor, dalbino, dcolor, dspotting, dtremor):
        menu.destroy()
        self.newLButton.configure(state=NORMAL)

        mAlbAnswer = self.yesNoConversion(malbino)
        dAlbAnswer = self.yesNoConversion(dalbino)

        if mAlbAnswer == True:
            mcolor = "Unknown"
            mspotting = "Unknown"

        if dAlbAnswer == True:
            dcolor = "Unknown"
            dspotting = "Unknown"

        # mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
        Main.total(self, "new", "new", self.offspringNum, "Female", mAlbAnswer, mcolor, mspotting, self.yesNoConversion(mtremor), "Male", dAlbAnswer, dcolor, dspotting, self.yesNoConversion(dtremor))

    def yesNoConversion(self, yesNoStr):
        if yesNoStr == "Yes":
            return True
        elif yesNoStr == "No":
            return False
        else:
            print("Yes/No was not passed in, something went wrong")

    # Function used when a bunny row is clicked. Displays info about that bunny.
    def changeSelectedBunny(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        # TODO: Conditionals for types of bunnies to determine picture. Maybe make this a separate function? Change BunnyPicture
        self.bunnyInfo["NumberLabel"].configure(text="Bunny # " + bunNum)
        self.bunnyInfo["BunnyPicLabel"].configure(image=self.bunnyInfo["BunnyPicture"])
        self.bunnyInfo["InfoLabel"].configure(text="Sex: "+ sex + "\nAlbino: " + albino + "\nColor: " + color + "\nPattern: " + pattern + "\nTremor: " + tremor)
        # TODO: If this doesn't work, reload them?