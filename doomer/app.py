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


# TODO: вынести конфиг в отдельный класс и работать с ним из сессии и других классов
def init_default_config():
    config_dict = dict()
    config_dict['wads_path'] = './wads'
    config_dict['pk3_path'] = './pk3s'
    config_dict['saves_path'] = './saves'
    config_dict['screenshots_path'] = './screenshots'
    config_dict['configs_path'] = './configs'
    config_dict['dooms'] = dict()

    with open('config.json', 'w') as config_file:
        json.dump(config_dict, config_file, indent=4)


def init_default_directories():
    for directory in DEFAULT_DIRS:
        if not os.path.exists(directory):
            os.makedirs(directory)


def run():
    root = Tk()

    init_default_directories()
    if not os.path.exists('./config.json'):
        init_default_config()

    with open('config.json') as config_file:
        config = json.load(config_file)

    session = Session(config)
    label = Label(root, text=str(session.wads_handler.wads_list))
    label.pack()
    root.mainloop()
