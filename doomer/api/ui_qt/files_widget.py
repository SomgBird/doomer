from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QListWidget, QHBoxLayout

from doomer.api.ui_qt.abs_frame import AbstractFrame


class FilesWidget(QWidget):
    def __init__(self, config, files_handler, name, *args, **kwargs):
        super(FilesWidget, self).__init__(*args, **kwargs)

        self._config = config
        self._files_handler = files_handler
        self._name = name

        self._files_layout = QHBoxLayout(self)
        self._files_listbox = QListWidget()
        self._files_layout.addWidget(self._files_listbox)
        self.setLayout(self._files_layout)

    def __update_files_handler(self, files_path):
        try:
            self._files_handler.read_files_dict(files_path)
            # self._files_label.config(text=self._files_handler.files_path)
        except FileNotFoundError:
            # tk.messagebox.showerror('Error!', self._name + ' directory not found!')
            # self._files_label.config(text=self._name + ' directory not found!')
            print('fh error')

    def update_files_listbox(self):
        """
        Update list of files
        :return: None
        """
        files_path = self._config.config_dict[str.lower(self._name) + '_path']
        self.__update_files_handler(files_path)

        self._files_listbox.clear()
        for wad_name in self._files_handler.files_dict.keys():
            self._files_listbox.insertItem(0, wad_name)
