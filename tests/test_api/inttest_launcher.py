import filecmp
import json
import os
from unittest import TestCase
from ddt import ddt, data, unpack

from doomer.api.files_handler import FilesHandler
from doomer.api.dooms_handler import DoomsHandler
from doomer.api.saves_handler import SavesHandler
from doomer.api.configs_handler import ConfigsHandler
from doomer.api.launcher import Launcher
from pathlib import Path

CASES_PATH = Path('D:/Dev/doomer/doomer/tests/test_api/inttest_launcher_cases/')
ZDOOM_PATH = 'D:\\Games\\DOOM\\zdoom\\zdoom.exe'


@ddt
class InttestLauncher(TestCase):
    @data(
        # Conf and Save
        (CASES_PATH / 'minimal/dooms.json',
         CASES_PATH / 'minimal/iwads',
         CASES_PATH / 'minimal/conf_save',
         CASES_PATH / 'minimal/conf_save',
         'zdoom.exe', 'DOOM.WAD',
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'minimal/iwads/DOOM.WAD'),
             '-savedir',
             str(CASES_PATH / 'minimal/conf_save/zdoom.exe_DOOM.WAD'),
             '-config',
             str(CASES_PATH / 'minimal/conf_save/zdoom.exe_DOOM.WAD.ini')
         ]),
        # No Conf and Save
        (CASES_PATH / 'minimal/dooms.json',
         CASES_PATH / 'minimal/iwads',
         CASES_PATH / 'minimal/noconf_save',
         CASES_PATH / 'minimal/noconf_save',
         'zdoom.exe', 'DOOM.WAD',
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'minimal/iwads/DOOM.WAD'),
             '-savedir',
             str(CASES_PATH / 'minimal/noconf_save/zdoom.exe_DOOM.WAD')
         ]),
    )
    @unpack
    def test_minimal_save(self, dooms_path, iwads_path, saves_path, configs_path, doom_name, iwad_name, expected):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(dooms_path)

        iwads_handler = FilesHandler({'wad': [b'IWAD'], 'WAD': [b'IWAD']})
        iwads_handler.read_files_dict(iwads_path)

        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(saves_path)

        configs_handler = ConfigsHandler()
        configs_handler.read_configs_dict(configs_path)

        launcher = Launcher(
            dooms_handler=dooms_handler,
            iwads_handler=iwads_handler,
            saves_handler=saves_handler,
            configs_handler=configs_handler
        )
        command = launcher.create_command(
            doom_name=doom_name,
            iwad_name=iwad_name
        )

        self.assertEqual(expected, command)

    @data(
        # No Conf and No Save
        (CASES_PATH / 'minimal/dooms.json',
         CASES_PATH / 'minimal/iwads',
         CASES_PATH / 'minimal/noconf_nosave',
         CASES_PATH / 'minimal/noconf_nosave',
         'zdoom.exe', 'DOOM.WAD',
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'minimal/iwads/DOOM.WAD'),
             '-savedir',
             str(CASES_PATH / 'minimal/noconf_nosave/zdoom.exe_DOOM.WAD')
         ]),
        # Cong and No Save
        (CASES_PATH / 'minimal/dooms.json',
         CASES_PATH / 'minimal/iwads',
         CASES_PATH / 'minimal/conf_nosave',
         CASES_PATH / 'minimal/conf_nosave',
         'zdoom.exe', 'DOOM.WAD',
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'minimal/iwads/DOOM.WAD'),
             '-savedir',
             str(CASES_PATH / 'minimal/conf_nosave/zdoom.exe_DOOM.WAD'),
             '-config',
             str(CASES_PATH / 'minimal/conf_nosave/zdoom.exe_DOOM.WAD.ini')
         ]),
    )
    @unpack
    def test_minimal_nosave(self, dooms_path, iwads_path, saves_path, configs_path, doom_name, iwad_name, expected):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(dooms_path)

        iwads_handler = FilesHandler({'wad': [b'IWAD'], 'WAD': [b'IWAD']})
        iwads_handler.read_files_dict(iwads_path)

        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(saves_path)

        configs_handler = ConfigsHandler()
        configs_handler.read_configs_dict(configs_path)

        launcher = Launcher(
            dooms_handler=dooms_handler,
            iwads_handler=iwads_handler,
            saves_handler=saves_handler,
            configs_handler=configs_handler
        )
        command = launcher.create_command(
            doom_name=doom_name,
            iwad_name=iwad_name
        )

        self.assertEqual(expected, command)

        os.rmdir(CASES_PATH / saves_path / 'zdoom.exe_DOOM.WAD')

    @data(
        # One PWAD
        (CASES_PATH / 'optional/dooms.json',
         CASES_PATH / 'optional/iwads',
         CASES_PATH / 'optional/conf_save',
         CASES_PATH / 'optional/conf_save',
         'zdoom.exe', 'DOOM.WAD',
         CASES_PATH / 'optional/pwads',
         ['ATTACK.WAD'],
         CASES_PATH / 'optional/pk3s',
         [],
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'optional/iwads/DOOM.WAD'),
             '-file',
             str(CASES_PATH / 'optional/pwads/ATTACK.WAD'),
             '-savedir',
             str(CASES_PATH / 'optional/conf_save/zdoom.exe_DOOM.WAD_ATTACK.WAD'),
             '-config',
             str(CASES_PATH / 'optional/conf_save/zdoom.exe_DOOM.WAD_ATTACK.WAD.ini')
         ]),
        # One PK3
        (CASES_PATH / 'optional/dooms.json',
         CASES_PATH / 'optional/iwads',
         CASES_PATH / 'optional/conf_save',
         CASES_PATH / 'optional/conf_save',
         'zdoom.exe', 'DOOM.WAD',
         CASES_PATH / 'optional/pwads',
         [],
         CASES_PATH / 'optional/pk3s',
         ['PB_Allow_SV_Cheats.pk3'],
         [
             ZDOOM_PATH,
             '-iwad',
             str(CASES_PATH / 'optional/iwads/DOOM.WAD'),
             '-file',
             str(CASES_PATH / 'optional/pk3s/PB_Allow_SV_Cheats.pk3'),
             '-savedir',
             str(CASES_PATH / 'optional/conf_save/zdoom.exe_DOOM.WAD_PB_Allow_SV_Cheats.pk3'),
             '-config',
             str(CASES_PATH / 'optional/conf_save/zdoom.exe_DOOM.WAD_PB_Allow_SV_Cheats.pk3.ini')
         ]),
    )
    @unpack
    def test_optional(self, dooms_path, iwads_path, saves_path, configs_path, doom_name, iwad_name,
                      pwads_path, pwads_names, pk3s_path, pk3s_names, expected):
        dooms_handler = DoomsHandler()
        dooms_handler.read_dooms(dooms_path)

        iwads_handler = FilesHandler({'wad': [b'IWAD'], 'WAD': [b'IWAD']})
        iwads_handler.read_files_dict(iwads_path)

        saves_handler = SavesHandler()
        saves_handler.read_saves_dict(saves_path)

        configs_handler = ConfigsHandler()
        configs_handler.read_configs_dict(configs_path)

        pwads_handler = FilesHandler({'wad': [b'PWAD'], 'WAD': [b'PWAD']})
        pwads_handler.read_files_dict(pwads_path)

        pk3s_handler = FilesHandler({'pk3': [b'PK'], 'PK3': [b'PK']})
        pk3s_handler.read_files_dict(pk3s_path)

        launcher = Launcher(
            dooms_handler=dooms_handler,
            iwads_handler=iwads_handler,
            pwads_handler=pwads_handler,
            pk3s_handler=pk3s_handler,
            saves_handler=saves_handler,
            configs_handler=configs_handler
        )
        command = launcher.create_command(
            doom_name=doom_name,
            iwad_name=iwad_name,
            pwad_names=pwads_names,
            pk3_names=pk3s_names
        )

        self.assertEqual(expected, command)
