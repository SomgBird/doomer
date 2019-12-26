import subprocess


class Launcher:
    def __init__(self, doom_path, iwad_path, pwads_path=None, pk3s_path=None, saves_path=None, config_path=None):
        self._doom_path = doom_path
        self._iwad_path = iwad_path
        self._pwads_path = pwads_path
        self._pk3s_path = pk3s_path
        self._saves_path = saves_path
        self._config_path = config_path

    def launch(self):
        """
        Launch Doom with user configuration
        :return: None
        """
        launch_command = []

        if self._doom_path is not None:
            launch_command.append(str(self._doom_path))
        else:
            raise FileNotFoundError

        launch_command.append('-iwad')
        if self._iwad_path is not None:
            launch_command.append(str(self._iwad_path))
        else:
            raise FileNotFoundError

        launch_command.append('-file')
        if self._pwads_path is not None and self._pwads_path != []:
            for pwad in self._pwads_path:
                launch_command.append(str(pwad))

        if self._pk3s_path is not None and self._pk3s_path != []:
            for pk3 in self._pk3s_path:
                launch_command.append(str(pk3))

        subprocess.Popen(launch_command)
