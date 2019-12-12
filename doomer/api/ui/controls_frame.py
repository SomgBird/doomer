import tkinter as tk
from abs_frame import AbstractFrame
from launcher import Launcher


class ControlsFrame(AbstractFrame):
    def __init__(self, window, config, side, dooms_frame, wads_frame, pk3_frame):
        """
        Controls frame constructor
        :param window: frame layout window
        :param config: Doomer config
        :param side: layout side
        :param dooms_frame: doom ports frame
        :param wads_frame: WAD files list frame
        :param pk3_frame: PK3 files list frame
        """
        super().__init__(window, config, side)
        self._dooms_frame = dooms_frame
        self._wads_frame = wads_frame
        self._pk3_frame = pk3_frame

        self._controls_frame = tk.LabelFrame(self._window, text='Controls')
        self._controls_frame.pack(padx=10, pady=10, side=self._side, fill=tk.X)

        self._launch_button = tk.Button(self._controls_frame, text='Launch', command=self.__launch)
        self._launch_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def __launch(self):
        """
        Launch chosen Doom with user setup
        :return: None
        """
        Launcher(doom_path=self._dooms_frame.active_doom_path,
                 wad_path=self._wads_frame.active_file_path,
                 pk3_path=self._pk3_frame.active_file_path
                 ).launch()
