import filecmp
from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.dooms_handler import DoomsHandler
from pathlib import Path

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/dooms_handler_cases/')


@ddt
class TestDoomsHandler(TestCase):
    @data(
        (CASES_PATH / 'empty.json', {}),
        (CASES_PATH / 'multiple_dooms.json',
         {
             'gzdoom.exe': Path('D:\\Games\\DOOM\\gzdoom\\gzdoom.exe'),
             'zdoom.exe': Path('D:\\Games\\DOOM\\zdoom\\zdoom.exe')
         })
    )
    @unpack
    def test_read_dooms(self, input_file, expected_dict):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(input_file)
        self.assertEqual(dooms_handler.dooms_dict, expected_dict)

    @data(
        (CASES_PATH / 'empty.json', [('test_name', Path('./test_path'))], {'test_name': Path('./test_path')}),
        (CASES_PATH / 'multiple_dooms.json', [('test_name', Path('./test_path'))],
         {
             'gzdoom.exe': Path('D:\\Games\\DOOM\\gzdoom\\gzdoom.exe'),
             'zdoom.exe': Path('D:\\Games\\DOOM\\zdoom\\zdoom.exe'),
             'test_name': Path('./test_path')
         }),
        (CASES_PATH / 'multiple_dooms.json',
         [
             ('test_name1', Path('./test_path1')),
             ('test_name2', Path('./test_path2')),
         ],
         {
             'gzdoom.exe': Path('D:\\Games\\DOOM\\gzdoom\\gzdoom.exe'),
             'zdoom.exe': Path('D:\\Games\\DOOM\\zdoom\\zdoom.exe'),
             'test_name1': Path('./test_path1'),
             'test_name2': Path('./test_path2')
         })
    )
    @unpack
    def test_add_doom(self, input_file, new_dooms, expected_dict):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(input_file)
        for name, path in new_dooms:
            dooms_handler.add_doom(path, name)
        self.assertEqual(dooms_handler.dooms_dict, expected_dict)

    @data(
        (CASES_PATH / 'empty.json', ['test_name'], {}),
        (CASES_PATH / 'multiple_dooms.json', ['zdoom.exe'], {'gzdoom.exe': Path('D:\\Games\\DOOM\\gzdoom\\gzdoom.exe')}),
        (CASES_PATH / 'multiple_dooms.json', ['zdoom.exe', 'gzdoom.exe'], {})
    )
    @unpack
    def test_delete_doom(self, input_file, dooms_to_delete, expected_dict):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(input_file)
        for name in dooms_to_delete:
            dooms_handler.delete_doom(name)
        self.assertEqual(dooms_handler.dooms_dict, expected_dict)

    @data(
        ([], CASES_PATH / 'empty.json'),
        ([
            ('gzdoom.exe', Path('D:\\Games\\DOOM\\gzdoom\\gzdoom.exe')),
            ('zdoom.exe', Path('D:\\Games\\DOOM\\zdoom\\zdoom.exe'))
        ], CASES_PATH / 'multiple_dooms.json')
    )
    @unpack
    def test_write_dooms(self, input_dooms, expected_file):
        dooms_handler = DoomsHandler()
        for name, path in input_dooms:
            dooms_handler.add_doom(path, name)
        dooms_handler.write_dooms(CASES_PATH / 'out/result.json')
        self.assertTrue(filecmp.cmp(CASES_PATH / 'out/result.json', expected_file))
