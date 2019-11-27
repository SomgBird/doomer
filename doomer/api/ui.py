import tkinter as tk
import tkinter.filedialog
from session import Session


class UI:
    def __init__(self, session: Session):
        self._session = session

        # Main windows init
        self._main_windows = tk.Tk()
        self._main_windows.geometry("500x500")
        self._main_windows.title('Doomer')

        # WADs management frame
        self._wads_frame = tk.LabelFrame(self._main_windows, text='WADs')
        self._wads_frame.pack(padx=10, pady=10, side=tk.LEFT)
        self._choose_wads_button = tk.Button(self._wads_frame,
                                             text='Choose WADs directory',
                                             command=self.__choose_wads_directory_dialog)
        self._choose_wads_button.pack()
        self._wads_label = tk.Label(self._wads_frame, text='None')
        self._wads_list_box = tk.Listbox(self._wads_frame, width=40, height=25)
        self._wads_label.pack()
        self._wads_list_box.pack()
        self.__update_wads_list_box()

        # Dooms management frame
        self._dooms_frame = tk.LabelFrame(self._main_windows, text='Dooms')
        self._dooms_frame.pack(padx=10, pady=10, side=tk.LEFT)
        self._add_dooms_button = tk.Button(self._dooms_frame,
                                           text='Add new Doom',
                                           command=self.__add_doom_dialog)
        self._add_dooms_button.pack()
        self._dooms_label = tk.Label(self._dooms_frame)
        self._dooms_list_box = tk.Listbox(self._dooms_frame, width=40, height=25)
        self._dooms_label.pack()
        self._dooms_list_box.pack()
        self.__update_dooms_list_box()

        self._main_windows.mainloop()

    def __choose_wads_directory_dialog(self):
        wads_path = tk.filedialog.askdirectory()
        self._session.update_wads_handler(wads_path)
        self._wads_label.config(text=self._session.wads_handler.wads_path)
        self.__update_wads_list_box()
        self._session.config.set_field('wads_path', wads_path)
        self._session.config.write_config()

    def __update_wads_list_box(self):
        self._wads_list_box.delete(0, tk.END)
        for wad in self._session.wads_handler.wads_list:
            self._wads_list_box.insert(0, wad.name)

    def __add_doom_dialog(self):
        doom_path = tk.filedialog.askopenfilename()
        print(doom_path)
        self._session.dooms_handler.add_doom(name='test', path=doom_path)
        self._session.dooms_handler.write_dooms()
        self.__update_dooms_list_box()

    def __update_dooms_list_box(self):
        self._dooms_list_box.delete(0, tk.END)
        for doom_name in self._session.dooms_handler.dooms_dict.keys():
            self._dooms_list_box.insert(0, doom_name)
