import Interactables
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

        self.currentMother = ""
        self.currentFather = ""
        # This is used to change what the button does when clicked based on if a litter already exists
        self.newLButton = ""

        self.createButtons()
        self.createBunnyInfo()

        # Create bunny table
        self.table = BunnyTable(self.root, self)
        # Create totals table
        self.totalTable = TotalsTable(self.root, self)
        # TODO: Temporary list of values that needs to be replaced with mothers/fathers
        self.motherTable = ["New", "1", "2", "3"]
        self.fatherTable = ["New", "4", "5", "6"]

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
        self.newLButton.configure(command=lambda: self.newParents())
        self.currentMother = ""
        self.currentFather = ""
        #self.motherTable = []
        #self.fatherTable = []

    # Activates after litterMenu is filled out and "okay" button is clicked.
    #TODO: HOOK UP WITH JOE'S STUFF.
    def generateNewLitter(self, menu, motherNum, fatherNum, offspringNum):
        menu.destroy()
        self.newLButton.configure(state=NORMAL)

        if motherNum == "New":
            # MotherNum gets passed in and becomes "parentType"
            Interactables.newBunnyMenu(self, self.root, "Mother")
        if fatherNum == "New":
            Interactables.newBunnyMenu(self, self.root, "Father")

        # Now new mother and father will be set by setNewInfo. Take this info and do something

        print(motherNum, fatherNum, offspringNum)
    
    # Pops up new father and new mother menu for initial litter creation
    # TODO:This can cause some bugs with the button being disabled.
    def newParents(self):
        Interactables.newBunnyMenu(self, self.root, "Mother")
        Interactables.newBunnyMenu(self, self.root, "Father")

    # TODO: HOOK UP WITH JOE'S STUFF.
    def setNewInfo(self, menu, albino, color, spotting, tremor, parentType):
        menu.destroy()
        self.newLButton.configure(state=NORMAL)

        self.newLButton.configure(command=lambda: Interactables.newLitterMenu(self, self.root))
        # Not sure what exactly is done with this info, but it's here now
        # Set this up at the end
        if parentType == "Mother":
            pass
            #self.currentMother = newMother
        if parentType == "Father":
            pass
            #self.currentFather = newFather

    # Function used when a bunny row is clicked. Displays info about that bunny.
    def changeSelectedBunny(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        # TODO: Conditionals for types of bunnies to determine picture. Maybe make this a separate function? Change BunnyPicture
        self.bunnyInfo["NumberLabel"].configure(text="Bunny # " + bunNum)
        self.bunnyInfo["BunnyPicLabel"].configure(image=self.bunnyInfo["BunnyPicture"])
        self.bunnyInfo["InfoLabel"].configure(text="Sex: "+ sex + "\nAlbino: " + albino + "\nColor: " + color + "\nPattern: " + pattern + "\nTremor: " + tremor)
        # TODO: If this doesn't work, reload them?