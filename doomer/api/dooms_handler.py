import os
import json
from pathlib import Path


class DoomsHandler:
    @property
    def dooms_dict(self):
        return self._dooms_dict

    def __init__(self, dooms_path):
        """
        DoomsHandler constructor
        :param dooms_path: path to file with list of Doom ports
        """
        self._dooms_path = Path(dooms_path)
        self._dooms_dict = dict()

        self.read_dooms()

    def write_dooms(self):
        with open(self._dooms_path, 'w') as dooms_file:
            json.dump(self._dooms_dict, dooms_file, indent=4)

    def read_dooms(self):
        if not os.path.exists(self._dooms_path):
            self.write_dooms()
        with open(self._dooms_path, 'r') as dooms_file:
            self._dooms_dict = json.load(dooms_file)

    def add_doom(self, path, name: str):
        """
        Add new Doom port to doomer
        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        self._dooms_dict[name] = path
        self.write_dooms()

    def delete_doom(self, name: str):
        """
        Delete Doom port from doomer
        :param name: Doom port name
        :return: None
        """
        self._dooms_dict.pop(name, None)
        self.write_dooms()
