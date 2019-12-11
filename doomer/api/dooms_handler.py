import json
import pathlib

from pathlib_json import PathJSONDecoder, PathJSONEncoder


class DoomsHandler:
    @property
    def dooms_dict(self):
        return self._dooms_dict

    def __init__(self):
        """
        DoomsHandler constructor/
        """
        self._dooms_dict = dict()

    def write_dooms(self, path):
        """
        Write current Dooms to json file
        :return:
        """
        with open(path, 'w') as dooms_file:
            json.dump(self._dooms_dict, dooms_file, cls=PathJSONEncoder, indent=4)

    def read_dooms(self, path):
        """
        Read dooms list from config
        :return: None
        """
        with open(path, 'r') as dooms_file:
            self._dooms_dict = json.load(dooms_file, cls=PathJSONDecoder)

    def add_doom(self, path, name: str):
        """
        Add new Doom port to doomer
        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        self._dooms_dict[name] = pathlib.Path(path)

    def delete_doom(self, name: str):
        """
        Delete Doom port from doomer
        :param name: Doom port name
        :return: None
        """
        self._dooms_dict.pop(name, None)
