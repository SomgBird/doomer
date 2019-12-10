import os
from pathlib import Path


class WADsHandler:
    @property
    def wads_dict(self):
        """
        :return: dict of all WADs files
        """
        return self._wads_dict

    @property
    def wads_path(self):
        """
        :return: path to WADs directory
        """
        return self._wads_path

    def __init__(self):
        """
        WADsHandler constructor.
        """
        self._wads_path = None
        self._wads_dict = dict()

    def __filter_wads(self, files_list):
        """
        Set list of WADs by parsing .wad or .WAD file extension
        :param files_list: list of all files in directory
        :return: list of WADs
        """
        wads_list = []

        for file in files_list:
            if file.endswith('.wad') or file.endswith('.WAD'):
                wads_list.append(self._wads_path / file)

        return wads_list

    def __set_wads_dict(self, files_list):
        """
        Set list of WADs by parsing .wad or .WAD file extension
        :param files_list: list of all files in directory
        :return: None
        """
        self._wads_dict = dict()
        wads_list = self.__filter_wads(files_list)

        for wad in wads_list:
            self._wads_dict[wad.name] = wad

    def read_wads_dict(self, path):
        self._wads_path = Path(path)
        self.__set_wads_dict(os.listdir(self._wads_path))
