import tkinter as tk
from Controller import Controller
from MainWindow import MainWindow


root = tk.Tk()
window = MainWindow(root)

controller = Controller(window)

# Main loop for window
root.mainloop()