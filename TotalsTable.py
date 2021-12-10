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
        self.addEntry("Albino", 4, 1)
        self.addEntry("Not Albino", 4, 2)
        self.addEntry("Black", 4, 3)
        self.addEntry("Gray", 4, 4)
        self.addEntry("Chocolate", 4, 5)
        self.addEntry("Lilac", 4, 6)
        self.addEntry("Charlie", 4, 7)
        self.addEntry("Broken", 4, 8)
        self.addEntry("Solid", 4, 9)
        self.addEntry("Tremor", 4, 10)
        self.addEntry("Healthy", 4, 11)
        self.addEntry("Total", 4, 12)

    def initialVals(self):
        self.showMale("#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#")
        self.showFemale("#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#")
        self.showTotals("#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#")
  
    # Row 1
    def showMale(self, albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total):
        self.addEntry("Male", 5, 0)
        self.addEntry(albino, 5, 1)
        self.addEntry(notalbino, 5, 2)
        self.addEntry(black, 5, 3)
        self.addEntry(gray, 5, 4)
        self.addEntry(chocolate, 5, 5)
        self.addEntry(lilac, 5, 6)
        self.addEntry(charlie, 5, 7)
        self.addEntry(broken, 5, 8)
        self.addEntry(solid, 5, 9)
        self.addEntry(tremor, 5, 10)
        self.addEntry(healthy, 5, 11)
        self.addEntry(total, 5, 12)

    # Row 2
    def showFemale(self, albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total):
        self.addEntry("Female", 6, 0)
        self.addEntry(albino, 6, 1)
        self.addEntry(notalbino, 6, 2)
        self.addEntry(black, 6, 3)
        self.addEntry(gray, 6, 4)
        self.addEntry(chocolate, 6, 5)
        self.addEntry(lilac, 6, 6)
        self.addEntry(charlie, 6, 7)
        self.addEntry(broken, 6, 8)
        self.addEntry(solid, 6, 9)
        self.addEntry(tremor, 6, 10)
        self.addEntry(healthy, 6, 11)
        self.addEntry(total, 6, 12)

    # Row 3
    def showTotals(self, albino, notalbino, black, gray, chocolate, lilac, charlie, broken, solid, tremor, healthy, total):
        self.addEntry("Total", 7, 0)
        self.addEntry(albino, 7, 1)
        self.addEntry(notalbino, 7, 2)
        self.addEntry(black, 7, 3)
        self.addEntry(gray, 7, 4)
        self.addEntry(chocolate, 7, 5)
        self.addEntry(lilac, 7, 6)
        self.addEntry(charlie, 7, 7)
        self.addEntry(broken, 7, 8)
        self.addEntry(solid, 7, 9)
        self.addEntry(tremor, 7, 10)
        self.addEntry(healthy, 7, 11)
        self.addEntry(total, 7, 12)

    # Adds the bunny info to the grid
    def addEntry(self, txt, r, c):
        e = Label(self.parent, text=txt, padx = 12, pady = 10)
        e.grid(row = r, column = c)