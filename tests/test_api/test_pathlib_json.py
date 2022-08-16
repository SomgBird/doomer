from unittest import TestCase
from ddt import ddt, data, unpack
import json
from api.pathlib_json import PathJSONDecoder, PathJSONEncoder
from pathlib import Path
import filecmp

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/pathlib_json_cases/')


@ddt
class TestPathlibJSON(TestCase):
    @data(
        ({},
         CASES_PATH / 'empty.json'),
        ({
             'key': Path('./test_path/')
         },
         CASES_PATH / 'single_key.json'),
        ({
             'key1': Path('./test_path_1/'),
             'key2': Path('./test_path_2/'),
             'key3': Path('./test_path_3/')
         },
         CASES_PATH / 'multiple_keys.json')
    )
    @unpack
    def test_PathJSONEncoder(self, input_dict, expected_file):
        with open(CASES_PATH/'out/result.json', 'w') as f:
            json.dump(input_dict, f, cls=PathJSONEncoder)
        self.assertTrue(filecmp.cmp(CASES_PATH/'out/result.json', expected_file))

    @data(
        (CASES_PATH / 'empty.json',
         {}),
        (CASES_PATH / 'single_key.json',
         {
             'key': Path('./test_path/')
         }),
        (CASES_PATH / 'multiple_keys.json',
         {
             'key1': Path('./test_path_1/'),
             'key2': Path('./test_path_2/'),
             'key3': Path('./test_path_3/')
         })
    )
    @unpack
    def test_PathJSONDecoder(self, input_file, expected_dict):
        with open(input_file, 'r') as f:
            self.assertEqual(json.load(f, cls=PathJSONDecoder), expected_dict)
