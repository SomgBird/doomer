import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from abs_frame import AbstractFrame


class WADsFrame(AbstractFrame):
    @property
    def active_wad(self):
        """
        :return: chosen WAD file
        """
        return self._wads_list_box.get(tk.ACTIVE)

    def __init__(self, window, session, side):
        """
        WADs frame constructor
        :param window: frame layout window
        :param session: Doomer session
        :param side: layout side
        """
        super().__init__(window, session, side)

        # WADs management frame
        self._wads_frame = tk.LabelFrame(self._window, text='WADs')
        self._wads_frame.pack(padx=10, pady=10, side=self._side)

        # Button to choose new WADs directory
        self._choose_wads_button = tk.Button(self._wads_frame,
                                             text='Choose WADs directory',
                                             command=self.__choose_wads_directory_dialog)
        self._choose_wads_button.pack()

        # Label with path to WADs directory
        self._wads_label = tk.Label(self._wads_frame, text=self._session.wads_handler.wads_path)
        self._wads_label.pack()

        # List of WADs
        self._wads_list_box = tk.Listbox(self._wads_frame, width=40, height=25)
        self._wads_list_box.pack()

    def __update_wads_handler(self, wads_path):
        try:
            self._session.wads_handler.read_wads_dict(wads_path)
            self._wads_label.config(text=self._session.wads_handler.wads_path)
        except FileNotFoundError:
            tk.messagebox.showerror('Error!', 'WADs directory not found!')
            self._wads_label.config(text='WADs directory not found!')

    def __choose_wads_directory_dialog(self):
        """
        Choose WADs directory from file system
        :return: None
        """
        wads_path = tk.filedialog.askdirectory()
        self.__update_wads_handler(wads_path)
        self._session.config.set_field('wads_path', wads_path)
        self._session.config.write_config()
        self.update_wads_list_box()

    def update_wads_list_box(self):
        """
        Update list of WAD files
        :return: None
        """
        wads_path = self._session.config.config_dict['wads_path']
        self.__update_wads_handler(wads_path)

        self._wads_list_box.delete(0, tk.END)
        for wad_name in self._session.wads_handler.wads_dict.keys():
            self._wads_list_box.insert(0, wad_name)
