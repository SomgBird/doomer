from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.files_handler import FilesHandler
from pathlib import Path

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/files_handler_cases/')


@ddt
class TestFilesHandler(TestCase):
    @data(
        (CASES_PATH / 'empty_dir', {}),
        (CASES_PATH / 'one_wad', {'DOOM.WAD':  CASES_PATH / 'one_wad' / 'DOOM.WAD'}),
        (CASES_PATH / 'non_wad_file', {}),
        (CASES_PATH / 'multiple_wads',
         {
             'DOOM.WAD': CASES_PATH / 'multiple_wads' / 'DOOM.WAD',
             'DOOM2.WAD': CASES_PATH / 'multiple_wads' / 'DOOM2.WAD',
             'SCENARIO 1231.wad': CASES_PATH / 'multiple_wads' / 'SCENARIO 1231.wad'
         }),
        (CASES_PATH / 'mixed_1',
         {
             'DOOM2.WAD': CASES_PATH / 'mixed_1' / 'DOOM2.WAD',
             'SCENARIO 1231.wad': CASES_PATH / 'mixed_1' / 'SCENARIO 1231.wad'
         }),
        (CASES_PATH / 'mixed_2',
         {
             'DOOM.WAD': CASES_PATH / 'mixed_2' / 'DOOM.WAD',
             'DOOM2.WAD': CASES_PATH / 'mixed_2' / 'DOOM2.WAD',
             'MEPHISTO.WAD': CASES_PATH / 'mixed_2' / 'MEPHISTO.WAD',
             'SCENARIO 1231.wad': CASES_PATH / 'mixed_2' / 'SCENARIO 1231.wad'
         }),
    )
    @unpack
    def test_wads_dict(self, files_path, expected_files):
        wads_handler = FilesHandler({'wad': [b'IWAD', b'PWAD'], 'WAD': [b'IWAD', b'PWAD']})
        wads_handler.read_files_dict(files_path)
        self.assertEqual(expected_files, wads_handler.files_dict)

    @data(
        (CASES_PATH / 'empty_dir', {}),
        (CASES_PATH / 'one_pk3',
         {
             'brightmaps.pk3': CASES_PATH / 'one_pk3' / 'brightmaps.pk3'
         }),
        (CASES_PATH / 'multiple_pk3s',
         {
             'brightmaps.pk3': CASES_PATH / 'multiple_pk3s' / 'brightmaps.pk3',
             'zd_extra.pk3': CASES_PATH / 'multiple_pk3s' / 'zd_extra.pk3'
         }),
        (CASES_PATH / 'non_pk3_file', {}),
        (CASES_PATH / 'mixed_pk3',
         {
             'brightmaps.pk3': CASES_PATH / 'mixed_pk3' / 'brightmaps.pk3',
             'zd_extra.pk3': CASES_PATH / 'mixed_pk3' / 'zd_extra.pk3'
         })
    )
    @unpack
    def test_pk3s_dict(self, files_path, expected_files):
        pk3s_handler = FilesHandler({'pk3': [b'PK'], 'PK3': [b'PK']})
        pk3s_handler.read_files_dict(files_path)
        self.assertEqual(expected_files, pk3s_handler.files_dict)
