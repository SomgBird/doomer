import os
from pathlib import Path


class SavesHandler:
    @property
    def saves_dict(self):
        return self._saves_dict

    def __init__(self):
        self._saves_path = None
        self._saves_dict = dict()

    def __set_saves_dict(self, files_list):
        self._saves_dict = dict()

        for file in files_list:
            if os.path.isdir(self._saves_path / file):
                self._saves_dict[file] = self._saves_path / file

    def __init_save_dir(self, name):
        path = self._saves_path/name
        os.mkdir(path)
        self._saves_dict[name] = path

    def read_saves_dict(self, path):
        self._saves_path = Path(path)
        self.__set_saves_dict(os.listdir(self._saves_path))

    def get_saves_dir(self, name):
        if name not in self._saves_dict.keys():
            self.__init_save_dir(name)
        return self._saves_dict[name]


