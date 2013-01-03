"""

Filename: window.py
Author: Jason Cramer

The GUI window for changing settings and other fun stuff.

"""

from Tkinter import *

class AppWindow:
    def __init__(self, master):
        
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = AppWindow(root)

root.mainloop()
