import configparser as cp
import os
from pathlib import Path


class ConfigHandler:
    @property
    def configs_dict(self):
        return self._configs_dict

    def __init__(self):
        self._configs_path = None
        self._configs_dict = dict()

    def __set_files_dict(self, files_list):
        self._configs_dict = dict()

        for file in files_list:
            if file.endswith('ini') or file.endswith('INI'):
                self._configs_dict[file] = self._configs_path / file

    def read_configs_dict(self, path):
        self._configs_path = Path(path)
        self.__set_files_dict(os.listdir(self._configs_path))
