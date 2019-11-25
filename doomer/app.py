import json
import os
from tkinter import *


from doomer.session import Session

DEFAULT_DIRS = [
    'wads',
    'pk3s',
    'saves',
    'screenshots',
    'configs',
    'dooms'
]


def init_default_directories():
    for directory in DEFAULT_DIRS:
        if not os.path.exists(directory):
            os.makedirs(directory)


def run():
    root = Tk()

    init_default_directories()

    session = Session()
    label = Label(root, text=str(session.wads_handler.wads_list))
    label.pack()
    root.mainloop()
