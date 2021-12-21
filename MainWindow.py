from tkinter import *

# Most widgets in MainWindow are created using the controller so they can be changed dynamically
class MainWindow(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        
        # Master is root   
        self.master = master
        self.master.resizable(False, False)
        self.master.title("BunGeney")

