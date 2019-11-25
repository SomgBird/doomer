import os
from tkinter import messagebox
from pathlib import Path


class WADsHandler:
    @property
    def wads_list(self):
        """
        :return: list of all WADs files
        """
        return self._wads_list

    def __set_wads_list(self, files_list):
        """
        Set list of WADs by parsing .wad or .WAD file extension
        :param files_list: list of all files in directory
        :return: None
        """
        self._wads_list = []

        for file in files_list:
            if file.endswith('.wad') or file.endswith('.WAD'):
                self._wads_list.append(self._wads_path / file)

    def __init__(self, config_dict):
        """
        WADsHandler constructor.
        :param config_dict: doomer configuration
        """
        self._wads_path = Path(config_dict['wads_path'])

        try:
            self.__set_wads_list(os.listdir(self._wads_path))
        except FileNotFoundError:
            self._wads_path = None
            messagebox.showerror('Path error!', 'Directory does not exist!')
