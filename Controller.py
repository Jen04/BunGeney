import Interactables
from Table import Table
from tkinter import *

class Controller:
    def __init__(self, view):
        #self.model = model
        self.view = view
        self.root = self.view.master
        self.bunnyInfo = {}
        # Creates the view's menu bar
        self.createButtons()
        self.createBunnyInfo()

        # Create table
        self.table = Table(self.root)
        # Set column lables
        self.table.addNormalRow("Bunny #", "Parents", "Sex", "Albino", "Color", "Pattern", "Tremor")

 
    def createButtons(self):
        Interactables.buttons(self, self.view, self.root)

    def createBunnyInfo(self):
        Interactables.bunnyInfo(self, self.root)


    def newLitter(self):
        print("New litter success")

    def clearLitters(self):
        print("Clear litters success")