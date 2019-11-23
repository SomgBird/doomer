import os
from pathlib import Path
from tkinter import messagebox


class WADsHandler:
    @property
    def wads_list(self):
        """
        :return: list of all WADs files
        :rtype: list
        """
        return self._wads_list

    @wads_list.setter
    def wads_list(self, value):
        self._wads_list = []

        for root, dirs, files in value:
            for file in files:
                if file.endswith('.wad') or file.endswith('.WAD'):
                    self.wads_list.append(self._wads_path/file)

    @property
    def wads_path_str(self):
        """
        :return: WADs files directory path
        :rtype: str
        """
        return self._wads_path_str

    def __init__(self, wads_path_str: str):
        """
        WADsHandler constructor.
        :param wads_path_str: WADs files directory path
        :type wads_path_str: str
        """
        self._wads_path_str = wads_path_str
        self._wads_path = Path(wads_path_str)

        try:
            self.wads_list = os.walk(self._wads_path)
        except FileNotFoundError:
            self._wads_path = None
            self._wads_list = []
            messagebox.showerror('Path error!', 'Directory does not exist!')

