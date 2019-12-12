import os
from pathlib import Path


class FilesHandler:
    @property
    def files_dict(self):
        """
        dict of all files files
        """
        return self._files_dict

    @property
    def files_path(self):
        """
        path to files directory
        """
        return self._files_path

    def __init__(self, ext_list):
        self._files_path = None
        self._files_dict = dict()
        self._ext_list = ext_list

    def __filter_files(self, files_list):
        filtered_files = []

        for file in files_list:
            for ext in self._ext_list:
                if file.endswith(ext):
                    filtered_files.append(self._files_path / file)

        return filtered_files

    def __set_files_dict(self, files_list):
        self._files_dict = dict()
        filtered_files = self.__filter_files(files_list)

        for file in filtered_files:
            self._files_dict[file.name] = file

    def read_files_dict(self, path):
        self._files_path = Path(path)
        self.__set_files_dict(os.listdir(self._files_path))
