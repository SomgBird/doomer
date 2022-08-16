import filecmp
import json
import os
from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.saves_handler import SavesHandler
from pathlib import Path

from pathlib_json import PathJSONDecoder

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/saves_cases/')


@ddt
class TestSavesHandler(TestCase):
    @data(
        (CASES_PATH / 'empty_dir', {}),
        (CASES_PATH / 'one_save_dir',
         {
             '1': CASES_PATH / 'one_save_dir/1'
         }),
        (CASES_PATH / 'multiple_saves_dir',
         {
             '1': CASES_PATH / 'multiple_saves_dir/1',
             '2': CASES_PATH / 'multiple_saves_dir/2',
             '3': CASES_PATH / 'multiple_saves_dir/3'
         }),
    )
    @unpack
    def test_read_saves_dict(self, path, expected):
        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(path)
        self.assertEqual(expected, saves_handler.saves_dict)

    @data(
        (CASES_PATH / 'get_existed_dir', '1',
         {
             '1': CASES_PATH / 'get_existed_dir/1',
             '2': CASES_PATH / 'get_existed_dir/2',
             '3': CASES_PATH / 'get_existed_dir/3'
         },
         ['1', '2', '3'])
    )
    @unpack
    def test_get_saves_dict(self, path, d, expected_dict, expected_dirs):
        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(path)
        result = saves_handler.get_saves_dir(d)
        self.assertEqual(result, CASES_PATH / 'get_existed_dir' / d)
        self.assertEqual(expected_dict, saves_handler.saves_dict)
        self.assertEqual(expected_dirs, [file for file in os.listdir(path) if os.path.isdir(path / file)])

    @data(
        (CASES_PATH / 'get_non-existed_dir', '4',
         {
             '1': CASES_PATH / 'get_non-existed_dir/1',
             '2': CASES_PATH / 'get_non-existed_dir/2',
             '3': CASES_PATH / 'get_non-existed_dir/3',
             '4': CASES_PATH / 'get_non-existed_dir/4'
         },
         ['1', '2', '3', '4'])
    )
    @unpack
    def test_get_new_saves_dict(self, path, d, expected_dict, expected_dirs):
        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(path)
        result = saves_handler.get_saves_dir(d)
        self.assertEqual(result, CASES_PATH / 'get_non-existed_dir' / d)
        self.assertEqual(expected_dict, saves_handler.saves_dict)
        self.assertEqual(expected_dirs, [file for file in os.listdir(path) if os.path.isdir(path / file)])
        os.rmdir(CASES_PATH / 'get_non-existed_dir' / d)
