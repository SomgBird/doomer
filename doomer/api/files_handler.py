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
    def __check_header(file, headers):
        try:
            if os.path.isfile(file):
                with open(file, 'rb') as file_bytes:
                    for h in headers:
                        try:
                            h_idx = headers.index(file_bytes.read(len(h)))
                        except ValueError:
                            continue
                        return headers[h_idx]
            return None
        except PermissionError:
            print("Cannot read file! Permission Error!")
            return None

    def __filter_func(self, file, ext, headers):
        h = FilesHandler.__check_header(self._files_path / file, headers)
        if file.endswith(ext) and h is not None:
            return h
        return None

    def __filter_files(self, files_list):
        filtered_files = []

        for file in files_list:
            for ext in self._filter_config.keys():
                h = self.__filter_func(file, str(ext), self._filter_config[ext])
                if h is not None:
                    filtered_files.append(self._files_path / file)
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
