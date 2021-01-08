import filecmp
import json
from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.configs_handler import ConfigHandler
from pathlib import Path

from pathlib_json import PathJSONDecoder

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/configs_cases/')


@ddt
class TestConfigsHandler(TestCase):
    @data(
        (CASES_PATH / 'empty_dir', {}),
        (CASES_PATH / 'one_config', {'1.ini': CASES_PATH / 'one_config/1.ini'}),
        (CASES_PATH / 'multiple_configs',
         {
             '1.ini': CASES_PATH / 'multiple_configs/1.ini',
             '2.ini': CASES_PATH / 'multiple_configs/2.ini'
         }),
        (CASES_PATH / 'non_config', {}),
        (CASES_PATH / 'mixed',
         {
             '1.ini': CASES_PATH / 'mixed/1.ini',
             '2.ini': CASES_PATH / 'mixed/2.ini'
         })
    )
    @unpack
    def test_read_configs_dict(self, path, expected):
        configs_handler = ConfigHandler()
        configs_handler.read_configs_dict(path)
        self.assertEqual(expected, configs_handler.configs_dict)
