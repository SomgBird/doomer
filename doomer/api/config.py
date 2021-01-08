import json
import os

from pathlib import Path

from doomer.api.pathlib_json import PathJSONEncoder, PathJSONDecoder


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
        self._default_len = 7
        self._default_fields = ['iwads_path', 'pwads_path', 'pk3s_path', 'saves_path',
                                'screenshots_path', 'configs_path', 'dooms_path']

    def init_default_config(self):
        config_dict = dict()
        config_dict['iwads_path'] = Path('./iwads')
        config_dict['pwads_path'] = Path('./pwads')
        config_dict['pk3s_path'] = Path('./pk3s')
        config_dict['saves_path'] = Path('./saves')
        config_dict['screenshots_path'] = Path('./screenshots')
        config_dict['configs_path'] = Path('./configs')
        config_dict['dooms_path'] = Path('./dooms.json')

        self._config_dict = config_dict

    def set_field(self, name, value):
        if name in self._config_dict.keys():
            self._config_dict[name] = Path(value)

    def write_config(self):
        with open(self._config_path, 'w') as config_file:
            json.dump(self._config_dict, config_file, cls=PathJSONEncoder)

    def read_config(self):
        with open(self._config_path, 'r') as config_file:
            self._config_dict = json.load(config_file, cls=PathJSONDecoder)

        if len(self._config_dict.keys()) != self._default_len:
            raise KeyError('Config file is corrupted!')

        for name in self._default_fields:
            if name not in self._config_dict.keys():
                raise KeyError('Config file is corrupted!')

