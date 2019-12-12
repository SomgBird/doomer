import os
import subprocess


class Launcher:
    def __init__(self, doom_path, wad_path, pk3_path=None, saves_path=None, config_path=None):
        """
        Launcher constructor
        :param doom_path: path to Doom
        :param wad_path: path to WAD file to launch
        :param pk3_path: path to pk3 file to launch
        :param saves_path: path to save files directory
        :param config_path: path to configuration file
        """
        self._doom_path = doom_path
        self._wad_path = wad_path
        self._pk3_path = pk3_path
        self._saves_path = saves_path
        self._config_path = config_path

    def launch(self):
        """
        Launch Doom with user configuration
        :return: None
        """
        launch_command = []

        if self._doom_path is not None:
            launch_command.append(f'\"{self._doom_path}\"')
        if self._pk3_path is not None:
            launch_command.append(f'\"{self._pk3_path}\"')
        if self._wad_path is not None:
            launch_command.append(f'\"{self._wad_path}\"')

        subprocess.Popen(' '.join(launch_command))
