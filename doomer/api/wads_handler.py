import os
from tkinter import messagebox


class WADsHandler:
    @property
    def wads_list(self):
        """
        :return: list of all WADs files
        """
        return self._wads_list

    @wads_list.setter
    def wads_list(self, value):
        self._wads_list = []

        for root, dirs, files in value:
            for file in files:
                if file.endswith('.wad') or file.endswith('.WAD'):
                    self.wads_list.append(self._wads_path/file)

    def __init__(self, wads_path):
        """
        WADsHandler constructor.
        :param wads_path: WADs files directory path
        """
        self._wads_path = wads_path

        try:
            self.wads_list = os.walk(self._wads_path)
        # Incorrect path to WADs files
        except FileNotFoundError:
            self._wads_path = None
            messagebox.showerror('Path error!', 'Directory does not exist!')

