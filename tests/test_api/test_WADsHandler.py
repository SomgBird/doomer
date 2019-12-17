from unittest import TestCase
from ddt import ddt, data, unpack
from doomer.api.files_handler import FilesHandler
from pathlib import Path

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/wads_handler_cases/')


# TODO: rework test
@ddt
class TestFilesHandler(TestCase):
    @data(
        (CASES_PATH / 'empty_dir', []),
        (CASES_PATH / 'one_wad', [CASES_PATH / 'one_wad' / '1.wad']),
        (CASES_PATH / 'non_wad_file', []),
        (CASES_PATH / 'multiple_wads',
         [
             CASES_PATH / 'multiple_wads' / '1.wad',
             CASES_PATH / 'multiple_wads' / '2.wad',
             CASES_PATH / 'multiple_wads' / '3.WAD'
         ]),
        (CASES_PATH / 'mixed_1',
         [
             CASES_PATH / 'mixed_1' / '1.wad',
             CASES_PATH / 'mixed_1' / '2.wad',
             CASES_PATH / 'mixed_1' / '3.WAD'
         ]),
        (CASES_PATH / 'mixed_2',
         [
             CASES_PATH / 'mixed_2' / '1.wad',
             CASES_PATH / 'mixed_2' / '2.wad',
             CASES_PATH / 'mixed_2' / '3.WAD'
         ]),
    )
    @unpack
    def test_wads_list(self, wads_path, expected_wads):
        pass
        # wads_handler = FilesHandler(wads_path)
        # self.assertEqual(wads_handler.fi, expected_wads)
