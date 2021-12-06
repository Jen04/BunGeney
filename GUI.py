import tkinter as tk
from Controller import Controller
from MainWindow import MainWindow

#model = ClassCollection.ClassCollection()

# App instance
root = tk.Tk()
# Size
#root.geometry("1000x900")
# Instance of main window
window = MainWindow(root)

#controller = Controller(model, window)
controller = Controller(window)

# Main loop for window
root.mainloop()