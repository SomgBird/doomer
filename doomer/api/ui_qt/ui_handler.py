import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QMainWindow, QHBoxLayout, QErrorMessage, \
    QMessageBox, QAbstractItemView

from doomer.api.config import Config
from doomer.api.files_handler import FilesHandler
from doomer.api.dooms_handler import DoomsHandler

from doomer.api.ui.controls_frame import ControlsFrame
from doomer.api.ui.dooms_frame import DoomsFrame
from doomer.api.ui_qt.files_widget import FilesWidget


class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self._config = Config()
        self._iwads_handler = FilesHandler({'wad': b'IWAD', 'WAD': b'IWAD'})
        self._pwads_handler = FilesHandler({'wad': b'PWAD', 'WAD': b'PWAD'})
        self._pk3s_handler = FilesHandler({'pk3': b'PK'})
        self._dooms_handler = DoomsHandler()

        self.resize(800, 650)
        self.setWindowTitle('Doomer')
        self._main_layout = QHBoxLayout()
        self._setup_layout = QHBoxLayout()
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

        self._setup_layout.addWidget(self._iwads_widget)
        self._setup_layout.addWidget(self._pwads_widget)
        self._setup_layout.addWidget(self._pk3s_widget)
        self._main_layout.addLayout(self._setup_layout)

        self._main_widget = QWidget()
        self._main_widget.setLayout(self._main_layout)
        self.setCentralWidget(self._main_widget)

        try:
            self._config.read_config()
        except json.JSONDecodeError or KeyError:
            self._config.init_default_config()
            self._config.write_config()
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Error!', 'Could not load config file! Default configuration will be used.')
        except FileNotFoundError:
            self._config.init_default_config()
            info_dialog = QMessageBox()
            info_dialog.about(self, 'Default settings!', 'It seems you are using Doomer first time or your config file '
                                                         'is corrupted. Doomer will load default config file.')

        self._iwads_widget.update_files_listbox()
        self._pwads_widget.update_files_listbox()
        self._pk3s_widget.update_files_listbox()
