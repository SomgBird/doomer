import filecmp
import json
from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.config import Config
from pathlib import Path

from pathlib_json import PathJSONDecoder

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/config_cases/')


@ddt
class TestConfig(TestCase):
    def test_read_config(self):
        config = Config(CASES_PATH / 'init_config.json')
        config.read_config()
        self.assertEqual(config.config_dict,
                         {"iwads_path": Path("iwads"),
                          "pwads_path": Path("pwads"),
                          "pk3s_path": Path("pk3s"),
                          "saves_path": Path("saves"),
                          "screenshots_path": Path("screenshots"),
                          "configs_path": Path("configs"),
                          "dooms_path": Path("dooms.json")
                          })

    @data(
        CASES_PATH / 'empty.json',
        CASES_PATH / 'wrong_config.json'
    )
    def test_read_config_exception(self, input_file):
        config = Config(input_file)
        with self.assertRaises(KeyError):
            config.read_config()

    @data(
        ('iwads_path', 'test', CASES_PATH / 'config_test_iwad_path.json'),
        ('some_field', 'test', CASES_PATH / 'init_config.json')
    )
    @unpack
    def test_set_field(self, name, value, expected_config):
        config = Config(CASES_PATH / 'init_config.json')
        config.read_config()
        config.set_field(name, value)
        expected = Config(expected_config)
        expected.read_config()
        self.assertEqual(config.config_dict, expected.config_dict)

    def test_write_default_config(self):
        config = Config(CASES_PATH / 'get_existed_dir/result.json')
        config.init_default_config()
        config.write_config()
        self.assertTrue(filecmp.cmp(CASES_PATH / 'get_existed_dir/result.json', CASES_PATH / 'init_config.json'))
