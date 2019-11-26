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

    @property
    def wads_path(self):
        """
        :return: path to WADs directory
        """
        return self._wads_path

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

    def __init__(self, path):
        """
        WADsHandler constructor.
        :param path: path to WADs files
        """
        self._wads_path = Path(path)

        self.read_wads_list()

    def read_wads_list(self):
        try:
            self.__set_wads_list(os.listdir(self._wads_path))
        except FileNotFoundError:
            messagebox.showerror('Path error!', 'WADs directory does not exist!')
