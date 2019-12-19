import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QGridLayout, QMainWindow, QHBoxLayout

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
        self._wads_handler = FilesHandler(['wad', 'WAD'])
        self._pk3_handler = FilesHandler(['pk3'])
        self._dooms_handler = DoomsHandler()

        self.resize(800, 650)
        self.setWindowTitle('Doomer')

        self._main_layout = QHBoxLayout()
        self._setup_layout = QHBoxLayout()
        self._wads_widget = FilesWidget(
                config=self._config,
                files_handler=self._wads_handler,
                name='WADs'
        )
        self._pk3_widget = FilesWidget(
                config=self._config,
                files_handler=self._pk3_handler,
                name='PK3s'
        )

        self._setup_layout.addWidget(self._wads_widget)
        self._setup_layout.addWidget(self._pk3_widget)
        self._main_layout.addLayout(self._setup_layout)

        self._main_widget = QWidget()
        self._main_widget.setLayout(self._main_layout)
        self.setCentralWidget(self._main_widget)

        try:
            self._config.read_config()
        except json.JSONDecodeError:
            self._config.init_default_config()
            self._config.write_config()
            # tk.messagebox.showerror('Error!', 'Could not load config file! Default configuration will be used.')
        except KeyError:
            self._config.init_default_config()
            # tk.messagebox.showinfo('Default settings!', 'It seems you are using Doomer first time or your config file '
            #                                             'is corrupted. Doomer will load default config file.')

        self._wads_widget.update_files_listbox()
        self._pk3_widget.update_files_listbox()


        # self._wads_frame = FilesFrame(
        #     window=self._main_window,
        #     config=self._config,
        #     side=1,
        #     files_handler=self._wads_handler,
        #     name='WADs'
        # )

