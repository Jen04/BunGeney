from tkinter import *

class BunnyTable(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        self.canvas = Canvas(self.parent, width=810, height=450)
        self.scroll = Scrollbar(self.parent, orient="vertical", command=self.canvas.yview)
        self.scrollFrame = Frame(self.canvas)

        self.scrollFrame.bind("<Configure>", self.changeScrollArea)

        self.canvas.create_window((0, 0), window=self.scrollFrame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll.set)

        self.canvas.grid(row = 1, column = 0, sticky=N, columnspan=7, rowspan=3)
        self.scroll.grid(column=7, row=1, sticky=NS, rowspan=3)

        self.canvas.grid_propagate(False)

    def changeScrollArea(self, e):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Adds the first row that labels the grid
    def addFirstRow(self):
        rowText = "Bunny #".ljust(15) + "Parents".ljust(15) + "Sex".ljust(15) + "Albino".ljust(15) + "Color".ljust(15) + "Pattern".ljust(15) + "Tremor".ljust(15)
        self.controller.rowList.insert(len(self.controller.rowList), Button(self.scrollFrame,  width=100, justify="left", bg="#c0c0c0", anchor=W, font='TkFixedFont', text=rowText, command=lambda: self.controller.bunnyInfo.setDefaults()))
        self.resetRows()

    # Adds a row with information about an individual bunny
    def addNormalRow(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        #rowTxt = self.adjSp(bunNum) + self.adjSp(bunParents) + self.adjSp(sex) + self.adjSp(albino) + self.adjSp(color) + self.adjSp(pattern) + self.adjSp(tremor)
        rowList = [bunNum, bunParents, sex, albino, color, pattern, tremor]
        rowTxt = ""
        for element in rowList:
            rowTxt += element.ljust(15, ' ')

        self.controller.rowList.insert(len(self.controller.rowList), Button(self.scrollFrame, text=rowTxt, justify="left", font='TkFixedFont', anchor=W, width=100, command=lambda: self.controller.changeSelectedBunny(bunNum, sex, albino, color, pattern, tremor)))
        self.resetRows()

    # Adds a row that displays info about the litter when clicked
    def addLitterRow(self, firstParent, secondParent):
        self.controller.rowList.insert(len(self.controller.rowList), Button(self.scrollFrame, font='TkFixedFont', text="Offspring of bunnies " + firstParent + " and " + secondParent))
        self.resetRows()


    # Called every time rows are changed. Re-displays rows
    def resetRows(self):
        # Unmaps labels
        for row in self.scrollFrame.children.values():
            row.grid_forget()

        # Sets them in new positions
        for i, e in enumerate(self.controller.rowList):
            e.grid(row = i, columnspan=6, sticky=W)

    def deleteAllRows(self):
        # Delete labels
        for e in self.controller.rowList:
            e.destroy()

        # Rowlist back to empty
        self.controller.rowList = []

    
    # For new rows that have to do with a new litter, make a button as the divider?

    