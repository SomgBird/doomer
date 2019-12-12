import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from abs_frame import AbstractFrame


class FilesFrame(AbstractFrame):
    @property
    def active_file(self):
        """
        :return: chosen file
        """
        return self._files_list_box.get(tk.ACTIVE)

    @property
    def active_file_path(self):
        """
        :return: path to chosen file
        """
        return self._files_handler.files_dict[self.active_file]

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
        self._files_frame = tk.LabelFrame(self._window, text=self._name + 's')
        self._files_frame.pack(padx=10, pady=10, side=self._side)

        # Button to choose new files directory
        self._choose_files_button = tk.Button(self._files_frame,
                                              text='Choose ' + self._name + ' directory',
                                              command=self.__choose_files_directory_dialog)
        self._choose_files_button.pack()

        # Label with path to files directory
        self._files_label = tk.Label(self._files_frame, text=self._files_handler.files_path)
        self._files_label.pack()

        # List of files
        self._files_list_box = tk.Listbox(self._files_frame, width=40, height=25)
        self._files_list_box.pack()

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
        files_path = tk.filedialog.askdirectory()
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
