import Interactables
import Main
from BunnyTable import BunnyTable
from TotalsTable import TotalsTable
from tkinter import *
from BunnyInfo import BunnyInfo

class Controller:
    def __init__(self, view):
        #self.model = model
        self.view = view
        self.root = self.view.master
  
        # Row list used within Table.py. All row buttons are contained within this
        self.rowList = []
        # Dropdown options when selecting info for a new bunny
        self.dropDownList = [["No", "Yes"], ["Black", "Gray", "Chocolate", "Lilac"], ["Broken", "Charlie", "Solid"]]

        self.createButtons()

        # Create bunny table
        self.table = BunnyTable(self.root, self)
        # Create totals table
        self.totalTable = TotalsTable(self.root, self)

        self.bunnyInfo = BunnyInfo(self.root, self)  
        self.infoSetup()

        # Set column lables for bunny table, set initial values for totals table
        self.tableSetup()

    def tableSetup(self):
        self.table.addFirstRow()
        self.totalTable.setUpTable()
    
    def infoSetup(self):
        self.bunnyInfo.createFields()
 
    # Creates some of the buttons on the GUI
    def createButtons(self):
        Interactables.buttons(self, self.root)

    # Adds the labels at the top of the table
    def newLitter(self):
        self.table.addFirstRow()

    # Clears litters from table
    # TODO: make sure this is clearing everything it should
    def clearLitters(self):
        self.table.deleteAllRows()
        self.tableSetup()
        self.motherTable = ["New"]
        self.fatherTable = ["New"]
        Main.clearValues()
        self.bunnyInfo.setDefaults()

    # Adds individual bunny to the table
    def addBunnyToTable(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        self.table.addNormalRow(bunNum, bunParents, sex, albino, color, pattern, tremor)

    # Activates after litterMenu is filled out and "okay" button is clicked.
    def setNewParentInfo(self, menu, albino, color, spotting, tremor, parentType, motherNum, fatherNum, offspringNum):
        # Check which parent is new, put zeroes for the other one or something
        menu.destroy()

        # mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
        if parentType == "Mother":
            Main.total(self, "new", fatherNum, self.offspringNum, "Female", albino, color, spotting, tremor, 0, 0, 0, 0, 0)

        elif parentType == "Father":
            Main.total(self, motherNum, "new", self.offspringNum, 0, 0, 0, 0, 0, "Male", albino, color, spotting, tremor)
        else:
            print("Something went wrong.")

    def setExistingBunnies(self, litterMenu, motherNum, fatherNum, offspringNum):
        litterMenu.destroy()
        Main.total(self, motherNum, fatherNum, offspringNum, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def setFirstGeneration(self, menu, malbino, mcolor, mspotting, mtremor, dalbino, dcolor, dspotting, dtremor, offspringNum):
        menu.destroy()

        mAlbAnswer = self.yesNoConversion(malbino)
        dAlbAnswer = self.yesNoConversion(dalbino)

        if mAlbAnswer == True:
            mcolor = "Unknown"
            mspotting = "Unknown"

        if dAlbAnswer == True:
            dcolor = "Unknown"
            dspotting = "Unknown"

        # mother, father, numb_os, msex, malbino, mcolor, mspotting, mtremor, dsex, dalbino, dcolor, dspotting, dtremor
        Main.total(self, "new", "new", offspringNum, "Female", mAlbAnswer, mcolor, mspotting, self.yesNoConversion(mtremor), "Male", dAlbAnswer, dcolor, dspotting, self.yesNoConversion(dtremor))

    def yesNoConversion(self, yesNoStr):
        if yesNoStr == "Yes":
            return True
        elif yesNoStr == "No":
            return False
        else:
            print("Yes/No was not passed in, something went wrong")

    # NOTE: FIX THE BROKEN GRAYED OUT BUTTON. 

    # Function used when a bunny row is clicked. Displays info about that bunny.
    def changeSelectedBunny(self, bunNum, sex, albino, color, pattern, tremor):

        # Finds the correct file name for picture. All pictures are saved in this format
        picStr = "Pictures/"
        if sex == "Female":
            picStr += "F"
        else:
            picStr += "M"

        if albino == "Albino":
            picStr += "Albino"
        else:
            picStr = picStr + color + pattern
        picStr += ".png"
        
        self.bunnyInfo.setNumberLbl(bunNum)
        self.bunnyInfo.setPic(picStr)
        self.bunnyInfo.setInfo(sex, albino, color, pattern, tremor)