import sys
import json

import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QMainWindow, QHBoxLayout, QErrorMessage, \
    QMessageBox, QAbstractItemView, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from doomer.api.config import Config
from doomer.api.files_handler import FilesHandler
from doomer.api.dooms_handler import DoomsHandler

from doomer.api.ui.controls_frame import ControlsFrame
from doomer.api.ui.dooms_frame import DoomsFrame
from doomer.api.ui_qt.files_widget import FilesWidget
from dooms_widget import DoomsWidget


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self._config = Config()
        self._iwads_handler = FilesHandler({'wad': [b'IWAD'], 'WAD': [b'IWAD']})
        self._pwads_handler = FilesHandler({'wad': [b'PWAD'], 'WAD': [b'PWAD']})
        self._pk3s_handler = FilesHandler({'pk3': [b'PK']})
        self._dooms_handler = DoomsHandler()

        self.setFixedSize(800, 650)
        self.setWindowTitle('Doomer')
        self._main_layout = QVBoxLayout()
        self._control_layout = QHBoxLayout()
        self._setup_layout = QHBoxLayout()

        self._run_button = QPushButton("Run")

        self._dooms_widget = DoomsWidget(
            config=self._config,
            dooms_handler=self._dooms_handler,
            name='games',
            dooms_key='dooms_path',
        )

        self._iwads_widget = FilesWidget(
            config=self._config,
            files_handler=self._iwads_handler,
            name='IWADs',
            files_key='iwads_path',
            selection_mode=QAbstractItemView.SingleSelection
        )
        self._pwads_widget = FilesWidget(
            config=self._config,
            files_handler=self._pwads_handler,
            name='PWADs',
            files_key='pwads_path',
            selection_mode=QAbstractItemView.ExtendedSelection
        )
        self._pk3s_widget = FilesWidget(
            config=self._config,
            files_handler=self._pk3s_handler,
            name='PK3s',
            files_key='pk3s_path',
            selection_mode=QAbstractItemView.ExtendedSelection
        )

        self._control_layout.addWidget(self._dooms_widget)

        self._run_button.setFixedSize(200, 200)
        self._control_layout.addWidget(self._run_button, alignment=Qt.AlignRight)

        self._setup_layout.addWidget(self._iwads_widget)
        self._setup_layout.addWidget(self._pwads_widget)
        self._setup_layout.addWidget(self._pk3s_widget)

        self._main_layout.addLayout(self._control_layout)
        self._main_layout.addLayout(self._setup_layout)

        self._main_widget = QWidget()
        self._main_widget.setLayout(self._main_layout)
        self.setCentralWidget(self._main_widget)

        try:
            self._config.read_config()
        except json.JSONDecodeError or KeyError or ValueError:
            self._config.init_default_config()
            self._config.write_config()
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Could not load config file! Default configuration will be used.')
            error_dialog.exec_()
        except FileNotFoundError:
            self._config.init_default_config()
            self._config.write_config()
            info_dialog = QMessageBox()
            info_dialog.about(self, 'It seems you are using Doomer first time or your config file '
                                    'is corrupted. Doomer will load default config file.')
            info_dialog.exec_()

        try:
            self._dooms_widget.update_dooms_listbox()
        except json.JSONDecodeError or KeyError or ValueError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Could not load dooms.json file!')
            error_dialog.exec_()
        except FileNotFoundError:
            info_dialog = QMessageBox()
            info_dialog.about(self, 'dooms.json file is missing! Add new doom to create new file!')
            info_dialog.exec_()

        self._iwads_widget.update_files_listbox()
        self._pwads_widget.update_files_listbox()
        self._pk3s_widget.update_files_listbox()
