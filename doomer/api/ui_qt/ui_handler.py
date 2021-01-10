import sys
import json

import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QMainWindow, QHBoxLayout, QErrorMessage, \
    QMessageBox, QAbstractItemView, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from configs_handler import ConfigsHandler
from doomer.api.config import Config
from doomer.api.files_handler import FilesHandler
from doomer.api.dooms_handler import DoomsHandler

from doomer.api.ui_qt.files_widget import FilesWidget
from dooms_widget import DoomsWidget
from launcher import Launcher
from saves_handler import SavesHandler


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self._config = Config()
        self._dooms_handler = DoomsHandler()
        self._iwads_handler = FilesHandler({'wad': [b'IWAD'], 'WAD': [b'IWAD']})
        self._pwads_handler = FilesHandler({'wad': [b'PWAD'], 'WAD': [b'PWAD']})
        self._pk3s_handler = FilesHandler({'pk3': [b'PK']})
        self._saves_handler = SavesHandler()
        self._configs_handler = ConfigsHandler()
        self._launcher = Launcher(
            self._dooms_handler,
            self._iwads_handler,
            self._pwads_handler,
            self._pk3s_handler,
            self._saves_handler,
            self._configs_handler
        )

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
        self._run_button.clicked.connect(self.__run_doom)

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
            info_dialog.showMessage('It seems you are using Doomer first time or your config file '
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
            info_dialog.showMessage('dooms.json file is missing! Add new doom to create new file!')
            info_dialog.exec_()

        self._saves_handler.read_saves_dict(self._config.config_dict['saves_path'])
        self._configs_handler.read_configs_dict(self._config.config_dict['configs_path'])

        self._iwads_widget.update_files_listbox()
        self._pwads_widget.update_files_listbox()
        self._pk3s_widget.update_files_listbox()

    def __run_doom(self):
        selected_doom = self._dooms_widget.selected

        if not selected_doom:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Select any doom!')
            error_dialog.exec_()
            return
        doom_name = selected_doom[0].text()

        selected_iwad = self._iwads_widget.selected

        if not selected_iwad:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Select any IWAD!')
            error_dialog.exec_()
            return
        iwad_name = selected_iwad[0].text()

        pwad_names = [i.text() for i in self._pwads_widget.selected]
        pk3_names = [i.text() for i in self._pk3s_widget.selected]

        command = self._launcher.create_command(doom_name, iwad_name, pwad_names, pk3_names)
        self._launcher.launch(command)

