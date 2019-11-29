import tkinter as tk
from controls_frame import ControlsFrame
from dooms_frame import DoomsFrame
from session import Session
from wads_frame import WADsFrame


class UI:
    def __init__(self, session: Session):
        """
        UI Constructor
        :param session: Doomer session
        """
        self._session = session

        # Main windows init
        self._main_window = tk.Tk()
        self._main_window.geometry("650x650")
        self._main_window.title('Doomer')

        # Frame for launcher setup frames
        self._setup_frame = tk.LabelFrame(self._main_window, text='Setup')
        self._setup_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        # Launcher setup frames
        self._wads_frame = WADsFrame(self._setup_frame, self._session, tk.LEFT)
        self._dooms_frame = DoomsFrame(self._setup_frame, self._session, tk.RIGHT)
        self._controls_frame = ControlsFrame(
            window=self._main_window,
            session=self._session,
            side=tk.TOP,
            dooms_frame=self._dooms_frame,
            wads_frame=self._wads_frame,
            pk3_frame=None
        )

        self._main_window.mainloop()
