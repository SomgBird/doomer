import os

from api.ui.ui_handler import UI
from session import Session

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

    session = Session()

    app_ui = UI(session)
