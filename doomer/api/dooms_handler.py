import os
import json
from pathlib import Path
from tkinter import messagebox


class DoomsHandler:
    @property
    def dooms_dict(self):
        return self._dooms_dict

    @property
    def fspath_dict(self):
        return self._fspath_dict

    def __init__(self, dooms_path):
        """
        DoomsHandler constructor
        :param dooms_path: path to file with list of Doom ports
        """
        self._dooms_path = Path(dooms_path)
        self._dooms_dict = dict()
        self._fspath_dict = dict()
        self.read_dooms()

    def write_dooms(self):
        """
        Write current Dooms to json file
        :return:
        """
        with open(self._dooms_path, 'w') as dooms_file:
            json.dump(self._fspath_dict, dooms_file, indent=4)

    def read_dooms(self):
        """
        Read dooms list from config
        :return: None
        """
        try:
            with open(self._dooms_path, 'r') as dooms_file:
                self._fspath_dict = json.load(dooms_file)

            self._dooms_dict = dict()
            for doom in self._fspath_dict.keys():
                self._dooms_dict[doom] = Path(self._fspath_dict[doom])
        except FileNotFoundError:
            messagebox.showerror('Path error!', 'Dooms list file does not exist!')

    def add_doom(self, path: str, name: str):
        """
        Add new Doom port to doomer
        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        self._dooms_dict[name] = Path(path)
        self._fspath_dict[name] = os.fspath(self._dooms_dict[name])

    def delete_doom(self, name: str):
        """
        Delete Doom port from doomer
        :param name: Doom port name
        :return: None
        """
        self._dooms_dict.pop(name, None)
        self._fspath_dict.pop(name, None)
