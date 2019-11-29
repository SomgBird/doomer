import tkinter as tk
import tkinter.filedialog


class DoomsFrame:
    @property
    def active_doom(self):
        return self._dooms_list_box.get(tk.ACTIVE)

    def __init__(self, window, session):
        self._window = window
        self._session = session

        self._dooms_frame = tk.LabelFrame(self._window, text='Dooms')
        self._dooms_frame.pack(padx=10, pady=10, side=tk.LEFT)
        self._add_dooms_button = tk.Button(self._dooms_frame,
                                           text='Add new Doom',
                                           command=self.__add_doom_dialog)
        self._add_dooms_button.pack()
        self._dooms_label = tk.Label(self._dooms_frame)
        self._dooms_label.pack()
        self._dooms_list_box = tk.Listbox(self._dooms_frame, width=40, height=25)
        self._dooms_list_box.pack()
        self.__update_dooms_list_box()

    def __add_doom_dialog(self):
        doom_path = tk.filedialog.askopenfilename()
        self._session.dooms_handler.add_doom(name='test', path=doom_path)
        self._session.dooms_handler.write_dooms()
        self.__update_dooms_list_box()

    def __update_dooms_list_box(self):
        self._dooms_list_box.delete(0, tk.END)
        for doom_name in self._session.dooms_handler.dooms_dict.keys():
            self._dooms_list_box.insert(0, doom_name)
