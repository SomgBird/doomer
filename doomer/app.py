from tkinter import *
from doomer.session import Session


def run():
    root = Tk()
    session = Session('./', None, None, None)
    label = Label(root, text=str(session.wads_handler.wads_list))
    label.pack()
    root.mainloop()
