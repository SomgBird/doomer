import tkinter as tk
import tkinter.filedialog
from session import Session
from launcher import Launcher
from wads_frame import WADsFrame
from dooms_frame import DoomsFrame


# TODO: вынести фреймы в отдельный классы в doomer.api.ui
class UI:
    def __init__(self, session: Session):
        self._session = session

        # Main windows init
        self._main_window = tk.Tk()
        self._main_window.geometry("600x600")
        self._main_window.title('Doomer')

        self._wads_frame = WADsFrame(self._main_window, self._session)
        self._dooms_frame = DoomsFrame(self._main_window, self._session)

        # Test launch button
        self._launch_button = tk.Button(self._main_window, text='Launch', command=self.__launch)
        self._launch_button.pack(side=tk.TOP)

        self._main_window.mainloop()

    def __launch(self):
        doom = self._session.dooms_handler.fspath_dict[self._dooms_frame.active_doom]
        chosen_wad = self._session.wads_handler.wads_dict[self._wads_frame.active_wad]

        launcher = Launcher(doom, chosen_wad)
        launcher.launch()

