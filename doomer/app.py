import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
#from doomer.api.ui.ui_handler import UI
from doomer.api.ui_qt.ui_handler import UI

DEFAULT_DIRS = [
    'iwads',
    'files',
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

    app = QApplication([])

    app_ui = UI()
    app_ui.show()

    sys.exit(app.exec_())
