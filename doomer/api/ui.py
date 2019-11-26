import tkinter
import tkinter.filedialog


class UI:
    def __init__(self, session):
        self._session = session

        # Main windows init
        self._main_windows = tkinter.Tk()
        self._main_windows.geometry("500x500")
        self._main_windows.title('Doomer')

        self._wads_label = tkinter.Label(self._main_windows, text='Choose WADs directory:')
        self._wads_label.pack()
        self._choose_wads_button = tkinter.Button(self._main_windows,
                                                  text='test',
                                                  command=self.__choose_wads_directory_dialog)
        self._choose_wads_button.pack()

        self._main_windows.mainloop()

    def __choose_wads_directory_dialog(self):
        wads_path = tkinter.filedialog.askdirectory()
        self._session.update_wads_handler(wads_path)
        self._wads_label.config(text=self._session.wads_handler.wads_path)
