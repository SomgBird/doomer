import os

from api.ui.ui_handler import UI

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
    init_default_directories()

    app_ui = UI()
