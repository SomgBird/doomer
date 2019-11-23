from tkinter import *
from doomer.session import Session


def run():
    session = Session('./', None, None, None)
    root = Tk()
    label = Label(root, text=str(session.wads_handler))
    label.pack()
    root.mainloop()
