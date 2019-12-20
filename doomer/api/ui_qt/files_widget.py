from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QListWidget, QHBoxLayout, QPushButton, QFileDialog, \
    QErrorMessage, QLabel, QAbstractItemView

from doomer.api.files_handler import FilesHandler
from doomer.api.config import Config


class FilesWidget(QWidget):
    def __init__(
            self,
            config: Config,
            files_handler: FilesHandler,
            name: str,
            files_key: str,
            selection_mode: QAbstractItemView.SelectionMode,
            *args,
            **kwargs
    ):
        # Widget setup
        super(FilesWidget, self).__init__(*args, **kwargs)

        self._config = config
        self._files_handler = files_handler
        self._name = name
        self._files_key = files_key
        self._selection_mode = selection_mode

        # Widget layout setup
        self._files_layout = QVBoxLayout()

        # Buttons
        # Choose files directory button
        self._buttons_layout = QHBoxLayout()
        self._choose_files_dir_button = QPushButton('Choose ' + name + ' directory', self)
        self._choose_files_dir_button.setMinimumHeight(40)
        self._choose_files_dir_button.clicked.connect(self.__choose_files_directory_dialog)
        self._buttons_layout.addWidget(self._choose_files_dir_button)

        # Clear selection button
        self._clear_selection_button = QPushButton('Clear selection', self)
        self._clear_selection_button.setMinimumHeight(40)
        self._clear_selection_button.clicked.connect(self.__clear_selection)
        self._buttons_layout.addWidget(self._clear_selection_button)

        self._files_layout.addLayout(self._buttons_layout)

        # Files path label
        self._path_label = QLabel()
        self._files_layout.addWidget(self._path_label)

        # Files list
        self._files_listbox = QListWidget()
        self._files_listbox.setSelectionMode(self._selection_mode)
        self._files_layout.addWidget(self._files_listbox)
        self.setLayout(self._files_layout)

    def __clear_selection(self):
        self._files_listbox.clearSelection()
        self._files_listbox.clearFocus()

    def __choose_files_directory_dialog(self):
        """
        Choose files directory from file system
        :return: None
        """
        options = QFileDialog.ShowDirsOnly
        files_path = QFileDialog.getExistingDirectory(parent=self,
                                                      caption='Choose ' + self._name + ' directory',
                                                      options=options)
        if files_path != '':
            self.__update_files_handler(files_path)
            self._config.set_field(self._files_key, files_path)
            self._config.write_config()
            self.update_files_listbox()

    def __update_files_handler(self, files_path):
        try:
            self._files_handler.read_files_dict(files_path)
            self._path_label.setText(str(self._files_handler.files_path))
        except FileNotFoundError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage(self._name + ' directory not found!')
            self._path_label.setText(self._name + ' directory not found!')

    def update_files_listbox(self):
        """
        Update list of files
        :return: None
        """
        files_path = self._config.config_dict[self._files_key]
        self.__update_files_handler(files_path)

        self._files_listbox.clear()
        for wad_name in self._files_handler.files_dict.keys():
            self._files_listbox.insertItem(0, wad_name)
