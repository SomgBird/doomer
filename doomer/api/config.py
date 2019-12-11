import json
import os
from pathlib import Path
from pathlib_json import PathJSONEncoder, PathJSONDecoder


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

    def init_default_config(self):
        config_dict = dict()
        config_dict['wads_path'] = Path('./wads')
        config_dict['pk3_path'] = Path('./pk3s')
        config_dict['saves_path'] = Path('./saves')
        config_dict['screenshots_path'] = Path('./screenshots')
        config_dict['configs_path'] = Path('./configs')
        config_dict['dooms_path'] = Path('./dooms.json')

        self._config_dict = config_dict
        self.write_config()

    def set_field(self, name, value):
        if name in self._config_dict.keys():
            self._config_dict[name] = Path(value)

    def write_config(self):
        with open(self._config_path, 'w') as config_file:
            json.dump(self._config_dict, config_file, cls=PathJSONEncoder, indent=4)

    def read_config(self):
        if not os.path.exists(self._config_path):
            self.init_default_config()

        with open(self._config_path, 'r') as config_file:
            self._config_dict = json.load(config_file, cls=PathJSONDecoder)

        if len(self._config_dict.keys()) == 0:
            raise KeyError('Config file is corrupted!')

