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

    def __init__(self, filter_config: dict):
        self._files_path = None
        self._files_dict = dict()
        self._filter_config = filter_config

    @staticmethod
    def __check_header(file, header):
        with open(file, 'rb') as file_bytes:
            if file_bytes.read(len(header)) == header:
                return True
        return False

    def __filter_func(self, file, ext, header):
        if file.endswith(ext) and FilesHandler.__check_header(self._files_path/file, header):
            return True
        return False

    def __filter_files(self, files_list):
        filtered_files = []

        for file in files_list:
            for ext in self._filter_config.keys():
                if self.__filter_func(file, str(ext), self._filter_config[ext]):
                    filtered_files.append(self._files_path/file)
                    break

        return filtered_files

    def __set_files_dict(self, files_list):
        self._files_dict = dict()
        filtered_files = self.__filter_files(files_list)

        for file in filtered_files:
            self._files_dict[file.name] = file

    def read_files_dict(self, path):
        self._files_path = Path(path)
        self.__set_files_dict(os.listdir(self._files_path))
