import subprocess

# https://zdoom.org/wiki/Command_line_parameters

from doomer.api.files_handler import FilesHandler
from doomer.api.dooms_handler import DoomsHandler
from doomer.api.saves_handler import SavesHandler
from doomer.api.configs_handler import ConfigsHandler


class Launcher:
    def __init__(self, dooms_handler: DoomsHandler, iwads_handler: FilesHandler, pwads_handler: FilesHandler = None,
                 pk3s_handler: FilesHandler = None, saves_handler: SavesHandler = None,
                 configs_handler: ConfigsHandler = None):
        self._dooms_handler = dooms_handler
        self._iwads_handler = iwads_handler
        self._pwads_handler = pwads_handler
        self._pk3s_handler = pk3s_handler
        self._saves_handler = saves_handler
        self._configs_handler = configs_handler

    def create_command(self, doom_name, iwad_name, pwad_names=None, pk3_names=None):
        launch_command = []
        name = ''

        if doom_name is not None:
            launch_command.append(str(self._dooms_handler.dooms_dict[doom_name]))
            name += doom_name
        else:
            raise FileNotFoundError

        launch_command.append('-iwad')
        if iwad_name is not None:
            launch_command.append(str(self._iwads_handler.files_dict[iwad_name]))
            name += '_' + iwad_name
        else:
            raise FileNotFoundError

        if pwad_names is not None and pwad_names != [] or pk3_names is not None and pk3_names != []:
            launch_command.append('-file')

        if pwad_names is not None and pwad_names != []:
            for pwad_name in pwad_names:
                launch_command.append(str(self._pwads_handler.files_dict[pwad_name]))
                name += '_' + pwad_name

        if pk3_names is not None and pk3_names != []:
            for pk3_name in pk3_names:
                launch_command.append(str(self._pk3s_handler.files_dict[pk3_name]))
                name += '_' + pk3_name

        launch_command.append('-savedir')
        launch_command.append(str(self._saves_handler.get_saves_dir(name)))

        config = self._configs_handler.get_config(name + '.ini')

        if config is not None:
            launch_command.append('-config')
            launch_command.append(str(config))

        return launch_command

    def launch(self, command):
        """
        Launch Doom with user configuration
        :return: None
        """
        subprocess.Popen(command)
