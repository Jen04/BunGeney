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

        self.createButtons()
        self.createBunnyInfo()

        # Create bunny table
        self.table = BunnyTable(self.root, self)
        # Create totals table
        self.totalTable = TotalsTable(self.root, self)
        # TODO: Temporary list of values that needs to be replaced with mothers/fathers
        self.motherTable = ["New", "1", "2", "3"]
        self.fatherTable = ["New", "4", "5", "6"]
        self.offspringTable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

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
    def clearLitters(self):
        self.table.deleteAllRows()
        self.tableSetup()

    # Activates after litterMenu is filled out and "okay" button is clicked.
    def generateNewLitter(self, motherNum, fatherNum, offspringNum):
        #if motherNum == "New":
            #motherData = Interactables.newBunnyMenu()
        #if fatherNum == "New":
            #fatherData = Interactables.newBunnyMenu()
        print(motherNum, fatherNum, offspringNum)

    # Function used when a bunny row is clicked. Displays info about that bunny.
    # TODO: Add all other parameters. Test with bunnyNum first.
    def changeSelectedBunny(self, bunnyNum):
        print(bunnyNum)