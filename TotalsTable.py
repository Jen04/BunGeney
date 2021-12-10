from tkinter import *

# Displays the computed data at the bottom of the window
class TotalsTable(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

    def setUpTable(self):
        self.topLabels()
        self.initialVals()

    def topLabels(self):
        self.addEntry("Sex", 4, 1)
        self.addEntry("Albino", 4, 2)
        self.addEntry("Color", 4, 3)
        self.addEntry("Pattern", 4, 4)
        self.addEntry("Tremor", 4, 5)

    def initialVals(self):
        self.showMale("#", "#", "#", "#", "#", "#")
        self.showFemale("#", "#", "#", "#", "#", "#")
        self.showTotals("#", "#", "#", "#", "#", "#")
  
    # Row 1
    def showMale(self, bunnyNum, sexTotal, albinoTotal, colorTotal, patternTotal, tremorTotal):
        self.addEntry("Male (" + bunnyNum + ")", 5, 0)
        self.addEntry(sexTotal, 5, 1)
        self.addEntry(albinoTotal, 5, 2)
        self.addEntry(colorTotal, 5, 3)
        self.addEntry(patternTotal, 5, 4)
        self.addEntry(tremorTotal, 5, 5)

    # Row 2
    def showFemale(self, bunnyNum, sexTotal, albinoTotal, colorTotal, patternTotal, tremorTotal):
        self.addEntry("Female (" + bunnyNum + ")", 6, 0)
        self.addEntry(sexTotal, 6, 1)
        self.addEntry(albinoTotal, 6, 2)
        self.addEntry(colorTotal, 6, 3)
        self.addEntry(patternTotal, 6, 4)
        self.addEntry(tremorTotal, 6, 5)

    # Row 3
    def showTotals(self, num, sexTotal, albinoTotal, colorTotal, patternTotal, tremorTotal):
        self.addEntry("Total (" + num + ")", 7, 0)
        self.addEntry(sexTotal, 7, 1)
        self.addEntry(albinoTotal, 7, 2)
        self.addEntry(colorTotal, 7, 3)
        self.addEntry(patternTotal, 7, 4)
        self.addEntry(tremorTotal, 7, 5)

    # Adds the bunny info to the grid
    def addEntry(self, txt, r, c):
        e = Label(self.parent, text=txt, padx = 10, pady = 10)
        e.grid(row = r, column = c)