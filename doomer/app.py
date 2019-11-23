from tkinter import *
from doomer.config_handler import a


def run():
    a()
    root = Tk()
    label = Label(root, text='test')
    label.pack()
    root.mainloop()
