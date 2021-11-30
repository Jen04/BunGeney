from tkinter import *

class Row(Frame):
    def __init__(self, parent, bunNum, bunParents, sex, albino, color, pattern, tremor):
        Frame.__init__(self, parent)

        self.bunNum = bunNum
        self.bunParents = bunParents
        self.sex = sex
        self.albino = albino
        self.color = color
        self.pattern = pattern
        self.tremor = tremor
        
        