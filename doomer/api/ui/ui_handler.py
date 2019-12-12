import json
import tkinter as tk
import tkinter.messagebox
from controls_frame import ControlsFrame
from dooms_frame import DoomsFrame
from session import Session
from files_frame import FilesFrame


class UI:
    def __init__(self, session: Session):
        """
        UI Constructor
        :param session: Doomer session
        """
        # Main windows init
        self._session = session
        self._main_window = tk.Tk()
        self._main_window.geometry("650x650")
        self._main_window.title('Doomer')

        # Frame for launcher setup frames
        self._setup_frame = tk.LabelFrame(self._main_window, text='Setup')
        self._setup_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Launcher setup frames
        self._wads_frame = FilesFrame(
            window=self._setup_frame,
            config=self._session.config,
            side=tk.LEFT,
            files_handler=self._session.wads_handler,
            name='WADs'
        )
        self._dooms_frame = DoomsFrame(
            window=self._setup_frame,
            config=self._session.config,
            side=tk.RIGHT,
            dooms_handler=self._session.dooms_handler)
        self._controls_frame = ControlsFrame(
            window=self._main_window,
            config=self._session.config,
            side=tk.TOP,
            dooms_frame=self._dooms_frame,
            wads_frame=self._wads_frame,
            pk3_frame=None
        )

        try:
            self._session.config.read_config()
        except json.JSONDecodeError:
            self._session.config.init_default_config()
            self._session.config.write_config()
            tk.messagebox.showerror('Error!', 'Could not load config file! Default configuration will be used.')
        except KeyError:
            self._session.config.init_default_config()
            tk.messagebox.showinfo('Default settings!', 'It seems you are using Doomer first time or your config file '
                                                        'is corrupted. Doomer will load default config file.')

        self._wads_frame.update_files_list_box()
        self._dooms_frame.update_dooms_list_box()
        self._main_window.mainloop()
