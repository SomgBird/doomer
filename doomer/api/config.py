import json
import os
from pathlib import Path


class Config:
    @property
    def config_dict(self):
        return self._config_dict

    def __init__(self, path=Path('./config.json')):
        """
        Config constructor
        :param path: path to doomer config file
        """
        self._config_path = path
        self._config_dict = None
        self.read_config()

    def init_default_config(self):
        config_dict = dict()
        config_dict['wads_path'] = './wads'
        config_dict['pk3_path'] = './pk3s'
        config_dict['saves_path'] = './saves'
        config_dict['screenshots_path'] = './screenshots'
        config_dict['configs_path'] = './configs'
        config_dict['dooms_path'] = './dooms.json'

        self._config_dict = config_dict
        self.write_config()

    def set_field(self, name, value):
        if name in self._config_dict.keys():
            self._config_dict[name] = value

    def write_config(self):
        with open(self._config_path, 'w') as config_file:
            json.dump(self._config_dict, config_file, indent=4)

    def read_config(self):
        if not os.path.exists(self._config_path):
            self.init_default_config()

        with open(self._config_path, 'r') as config_file:
            self._config_dict = json.load(config_file)
