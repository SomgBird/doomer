import pathlib

from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QListWidget, QHBoxLayout, QPushButton, QFileDialog, \
    QErrorMessage, QLabel, QAbstractItemView

from doomer.api.dooms_handler import DoomsHandler
from doomer.api.config import Config


class DoomsWidget(QWidget):
    @property
    def selected(self):
        return self._dooms_listbox.selectedItems()

    def __init__(
            self,
            config: Config,
            dooms_handler: DoomsHandler,
            name: str,
            dooms_key: str,
            *args,
            **kwargs
    ):
        # Dooms widget setup
        super(DoomsWidget, self).__init__(*args, **kwargs)

        self._config = config
        self._dooms_handler = dooms_handler
        self._name = name
        self._dooms_key = dooms_key

        # Widget layout setup
        self._dooms_layout = QVBoxLayout()

        # Buttons
        self._buttons_layout = QHBoxLayout()

        # Add doom button
        self._add_doom_button = QPushButton('Add', self)
        self._add_doom_button.setMinimumHeight(40)
        self._add_doom_button.clicked.connect(self.__add_doom)
        self._buttons_layout.addWidget(self._add_doom_button)

        # Delete doom button
        self._remove_doom_button = QPushButton('Remove', self)
        self._remove_doom_button.setMinimumHeight(40)
        self._remove_doom_button.clicked.connect(self.__remove_doom)
        self._buttons_layout.addWidget(self._remove_doom_button)

        self._dooms_layout.addLayout(self._buttons_layout)

        # Dooms list
        self._dooms_listbox = QListWidget()
        self._dooms_listbox.setSelectionMode(QAbstractItemView.SingleSelection)
        self._dooms_layout.addWidget(self._dooms_listbox)
        self.setLayout(self._dooms_layout)

    def __add_doom(self):
        doom_path = QFileDialog.getOpenFileName(parent=self,
                                                caption='Choose ' + self._name + ' directory',
                                                filter="Executable files (*.exe)")[0]
        if doom_path != '':
            doom_path = pathlib.Path(doom_path)

            if doom_path.name in [self._dooms_listbox.item(i).text() for i in range(self._dooms_listbox.count())]:
                error_dialog = QErrorMessage()
                error_dialog.showMessage(self._name + ' already added!')
                error_dialog.exec_()
                return

            self._dooms_handler.add_doom(doom_path, doom_path.name)
            self._dooms_handler.write_dooms(self._config.config_dict[self._dooms_key])
            self.update_dooms_listbox()

    def __remove_doom(self):
        selected = self._dooms_listbox.selectedItems()

        if selected == []:
            return

        name = selected[0].text()

        self._dooms_handler.delete_doom(name)
        self._dooms_handler.write_dooms(self._config.config_dict[self._dooms_key])
        self.update_dooms_listbox()

    def __update_dooms_handler(self, dooms_path):
        try:
            self._dooms_handler.read_dooms(dooms_path)
        except FileNotFoundError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage(self._name + ' directory not found!')
            error_dialog.exec_()

    def update_dooms_listbox(self):
        """
        Update list of files
        :return: None
        """
        dooms_path = self._config.config_dict[self._dooms_key]
        self.__update_dooms_handler(dooms_path)

        self._dooms_listbox.clear()
        for doom_name in self._dooms_handler.dooms_dict.keys():
            self._dooms_listbox.insertItem(0, doom_name)
        self._dooms_listbox.sortItems()
