from tkinter import *

class Table(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.gridFrame = Frame(self.parent)
        self.gridFrame.grid(row = 1, column = 0, sticky=N)

        self.rowList = []

    def addNormalRow(self, bunNum, bunParents, sex, albino, color, pattern, tremor):
        self.rowList.insert(len(self.rowList), Label(self.gridFrame, text=bunNum + bunParents + sex + albino + color + pattern + tremor))

        for row in self.gridFrame.children.values():
            row.grid_forget()

        for i, e in enumerate(self.rowList):
            e.grid(row = i)

    
    # For new rows that have to do with a new litter, make a button as the divider?

    