from os import listdir
from pathlib import Path


class WADsHandler:
    @property
    def get_wads_list(self):
        """
        :return: list of all WADs files
        :rtype: list
        """
        return self._wads_list

    @property
    def get_wads_path(self):
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
        self._wads_list = listdir(self._wads_path)
