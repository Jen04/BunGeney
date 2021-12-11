import Menus
import Main
import Counter
from BunnyTable import BunnyTable
from TotalsTable import TotalsTable
from tkinter import *
from BunnyInfo import BunnyInfo
import tkinter.font as font

class Controller:
    def __init__(self, view):
        self.view = view
        self.root = self.view.master
  
        # Row list used within BunnyTable.py
        self.rowList = []

        # Dropdown options when selecting info for a new bunny
        self.dropDownList = [["No", "Yes"], ["Black", "Gray", "Chocolate", "Lilac"], ["Broken", "Charlie", "Solid"]]

        # Add buttons to GUI
        self.createButtons()

        # Create bunny table
        self.table = BunnyTable(self.root, self)

        # Create totals table
        self.totalsTable = TotalsTable(self.root, self)

        # Info about individual bunnies
        self.bunnyInfo = BunnyInfo(self.root, self)  
        self.infoSetup()

        # Set column lables for bunny table, set initial values for totals table
        self.tableSetup()

    # Adds first row of bunnyTable, sets up totalTable
    def tableSetup(self):
        self.table.addFirstRow()
        self.totalsTable.setUpTable()
    
    # Creates widgets for bunnyInfo
    def infoSetup(self):
        self.bunnyInfo.createFields()

    # Clears litters from table
    # TODO: make sure this is clearing everything it should, and test clear
    # TODO: Scroll bar breaks when this is clicked if you're scrolled down. 
    def clearLitters(self):
        self.table.deleteAllRows()
        self.tableSetup()
        self.motherTable = ["New"]
        self.fatherTable = ["New"]
        Main.clearValues()
        self.bunnyInfo.setDefaults()
        self.table.canvas.yview_moveto('0.0')

    # Creates some of the buttons on the GUI
    def createButtons(self):
        fontSettings = font.Font(size = 12)

        # New Litter
        newLButton = Button(self.root, text="New Litter", command=lambda: Menus.newLitterMenu(self, self.root, Main.pot_mothers(), Main.pot_fathers()))
        newLButton['font'] = fontSettings
        newLButton.grid(row = 0, column = 0, pady = 10, padx = 10, sticky=W, columnspan=2)

        # Clear Litters
        newCButton = Button(self.root, text="Clear All Litters", command=lambda: self.clearLitters())
        newCButton['font'] = fontSettings
        newCButton.grid(row = 0, column = 3, pady = 10, padx = 10, sticky=W, columnspan=2)

    # Adds individual bunny to the table
    def addBunnyToTable(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        self.table.addNormalRow(bunNum, bunParents, sex, albino, color, pattern, tremor)

    # Activates after litterMenu is filled out and "okay" button is clicked. Sends data to Main.py
    def setNewParentInfo(self, menu, albino, color, spotting, tremor, parentType, motherNum, fatherNum, offspringNum):
        menu.destroy()

        if parentType == "Mother":
            Main.total(self, "new", fatherNum, offspringNum, "Female", self.yesNoConversion(albino), color, spotting, self.yesNoConversion(tremor), 0, 0, 0, 0, 0)
        else:
            Main.total(self, motherNum, "new", offspringNum, 0, 0, 0, 0, 0, "Male", self.yesNoConversion(albino), color, spotting, self.yesNoConversion(tremor))

    # Creates new bunnies based on existing bunnies
    def setExistingBunnies(self, litterMenu, motherNum, fatherNum, offspringNum):
        litterMenu.destroy()
        Main.total(self, motherNum, fatherNum, offspringNum, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    def getLitterInfo(self, litterNumber):
        litterCount = Counter.count(litterNumber)
        albino = litterCount[1][0][0]
        notalbino = litterCount[1][1][0]
        black = litterCount[2][0][0]
        gray = litterCount[2][1][0]
        chocolate = litterCount[2][2][0]
        lilac = litterCount[2][3][0]
        charlie = litterCount[3][0][0]
        broken = litterCount[3][1][0]
        solid = litterCount[3][2][0]
        tremor = litterCount[4][0][0]
        healthy = litterCount[4][1][0]
        total = litterCount[0][0]
        self.totalsTable.showMale(albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total)

        albino = litterCount[1][0][1]
        notalbino = litterCount[1][1][1]
        black = litterCount[2][0][1]
        gray = litterCount[2][1][1]
        chocolate = litterCount[2][2][1]
        lilac = litterCount[2][3][1]
        charlie = litterCount[3][0][1]
        broken = litterCount[3][1][1]
        solid = litterCount[3][2][1]
        tremor = litterCount[4][0][1]
        healthy = litterCount[4][1][1]
        total = litterCount[0][1]
        self.totalsTable.showFemale(albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total)

        albino = litterCount[1][0][2]
        notalbino = litterCount[1][1][2]
        black = litterCount[2][0][2]
        gray = litterCount[2][1][2]
        chocolate = litterCount[2][2][2]
        lilac = litterCount[2][3][2]
        charlie = litterCount[3][0][2]
        broken = litterCount[3][1][2]
        solid = litterCount[3][2][2]
        tremor = litterCount[4][0][2]
        healthy = litterCount[4][1][2]
        total = litterCount[0][2]
        self.totalsTable.showTotals(albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total)

    def addLitter(self, mother, father, litterNumber):
        self.table.addLitterRow(mother, father, litterNumber)

    def addTwoParentSeparator(self, mother, father):
        self.table.addTwoParentRow(mother, father)

    def addMotherSeparator(self, mother):
        self.table.addMotherRow(mother)

    def addFatherSeparator(self, father):
        self.table.addFatherRow(father)

    # Sends data to main from new mother and father
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

        Main.total(self, "new", "new", offspringNum, "Female", mAlbAnswer, mcolor, mspotting, self.yesNoConversion(mtremor), "Male", dAlbAnswer, dcolor, dspotting, self.yesNoConversion(dtremor))

    # Converts strings to the format Main.py expects before passing them in
    def yesNoConversion(self, yesNoStr):
        if yesNoStr == "Yes":
            return True
        elif yesNoStr == "No":
            return False
        else:
            print("Yes/No was not passed in, something went wrong")

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