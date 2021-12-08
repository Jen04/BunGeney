from tkinter import *

class BunnyTable(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller
        self.gridFrame = Frame(self.parent)
        self.gridFrame.grid(row = 1, column = 0, sticky=N, columnspan=6, rowspan=2)

    # Adds the first row that labels the grid
    def addFirstRow(self):
        rowText = self.adjSp("Bunny #") + self.adjSp("Parents") + self.adjSp("Sex") + self.adjSp("Albino") + self.adjSp("Color") + self.adjSp("Pattern") + self.adjSp("Tremor")
        self.controller.rowList.insert(len(self.controller.rowList), Button(self.gridFrame, text=rowText))
        self.resetRows()

    # Adjust string formatting so it shows up in the table correctly. All strings within the table will span at least 15 characters
    def adjSp(self, stri):
        offset = 15 - len(stri)
        return stri + ' ' * offset

    # Adds a row with information about an individual bunny
    def addNormalRow(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        self.controller.rowList.insert(len(self.controller.rowList), Button(self.gridFrame, text=self.adjSp(bunNum) + self.adjSp(bunParents) + self.adjSp(sex) + self.adjSp(albino) + self.adjSp(color) + self.adjSp(pattern) + self.adjSp(tremor), command=lambda: self.controller.changeSelectedBunny(bunNum, bunParents, sex, albino, color, pattern, tremor)))
        self.resetRows()

    # Adds a row that displays info about the litter when clicked
    def addLitterRow(self, firstParent, secondParent):
        self.controller.rowList.insert(len(self.controller.rowList), Button(self.gridFrame, text="Offspring of bunnies " + firstParent + " and " + secondParent))
        self.resetRows()

    # Called every time rows are changed. Re-displays rows
    def resetRows(self):
        # Unmaps labels
        for row in self.gridFrame.children.values():
            row.grid_forget()

        # Sets them in new positions
        for i, e in enumerate(self.controller.rowList):
            e.grid(row = i)

    def deleteAllRows(self):
        # Delete labels
        for e in self.controller.rowList:
            e.destroy()

        # Rowlist back to empty
        self.controller.rowList = []

    
    # For new rows that have to do with a new litter, make a button as the divider?

    