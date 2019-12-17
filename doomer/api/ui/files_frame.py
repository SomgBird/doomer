import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog

from pathlib import Path

from doomer.api.ui.abs_frame import AbstractFrame


class FilesFrame(AbstractFrame):
    @property
    def active_file(self):
        """
        :return: chosen file
        """
        if len(self._files_list_box.curselection()) != 0:
            return self._files_list_box.get(self._files_list_box.curselection())
        return None

    @property
    def active_file_path(self):
        """
        :return: path to chosen file
        """
        active = self._files_handler.files_dict.get(self.active_file, None)
        if active is not None:
            return Path(active)
        return None

    def __init__(self, window, config, side, files_handler, name):
        """
        files frame constructor
        :param window: frame layout window
        :param config: Doomer config
        :param side: layout side
        """
        super().__init__(window, config, side)
        self._files_handler = files_handler
        self._name = name

        # files management frame
        self._files_frame = tk.LabelFrame(self._window, text=self._name)
        self._files_frame.pack(padx=10, pady=10, side=self._side)

        # Button to choose new files directory
        self._choose_files_button = tk.Button(
            self._files_frame,
            text='Choose ' + self._name + ' directory',
            command=self.__choose_files_directory_dialog
        )
        self._choose_files_button.pack()

        self._clear_selection_button = tk.Button(
            self._files_frame,
            text='Clear',
            command=self.__clear_selection
        )
        self._clear_selection_button.pack()

        # Label with path to files directory
        self._files_label = tk.Label(
            self._files_frame,
            text=self._files_handler.files_path
        )
        self._files_label.pack()

        # List of files
        self._files_list_box = tk.Listbox(
            self._files_frame,
            width=40, height=25,
            selectmode=tk.SINGLE,
            exportselection=False
        )
        self._files_list_box.pack()

    def __clear_selection(self):
        self._files_list_box.selection_clear(self._files_list_box.curselection())

    def __update_files_handler(self, files_path):
        try:
            self._files_handler.read_files_dict(files_path)
            self._files_label.config(text=self._files_handler.files_path)
        except FileNotFoundError:
            tk.messagebox.showerror('Error!', self._name + ' directory not found!')
            self._files_label.config(text=self._name + ' directory not found!')

    def __choose_files_directory_dialog(self):
        """
        Choose files directory from file system
        :return: None
        """
        print(self._files_list_box.get(self._files_list_box.curselection()))
        files_path = tk.filedialog.askdirectory()
        if files_path != '':
            self.__update_files_handler(files_path)
            self._config.set_field(str.lower(self._name) + '_path', files_path)
            self._config.write_config()
            self.update_files_list_box()

    def update_files_list_box(self):
        """
        Update list of files
        :return: None
        """
        files_path = self._config.config_dict[str.lower(self._name) + '_path']
        self.__update_files_handler(files_path)

        self._files_list_box.delete(0, tk.END)
        for wad_name in self._files_handler.files_dict.keys():
            self._files_list_box.insert(0, wad_name)
