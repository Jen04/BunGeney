from tkinter import *

# Inherits from frame class in tkinter
class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        
        # Master is root   
        self.master = master
        self.setup()

    def setup(self):
        self.master.title("Inheritance Lab")

