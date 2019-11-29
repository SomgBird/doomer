import tkinter as tk
import tkinter.filedialog


class WADsFrame:
    @property
    def active_wad(self):
        return self._wads_list_box.get(tk.ACTIVE)

    def __init__(self, window, session):
        self._window = window
        self._session = session

        # WADs management frame
        self._wads_frame = tk.LabelFrame(self._window, text='WADs')
        self._wads_frame.pack(padx=10, pady=10, side=tk.LEFT)

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

        # Update wads
        self.__update_wads_list_box()

    def __update_wads_list_box(self):
        self._wads_list_box.delete(0, tk.END)
        for wad_name in self._session.wads_handler.wads_dict.keys():
            self._wads_list_box.insert(0, wad_name)

    def __choose_wads_directory_dialog(self):
        wads_path = tk.filedialog.askdirectory()
        self._session.update_wads_handler(wads_path)
        self._wads_label.config(text=self._session.wads_handler.wads_path)
        self._session.config.set_field('wads_path', wads_path)
        self._session.config.write_config()

        self.__update_wads_list_box()
