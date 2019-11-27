import os


class Launcher:
    def __init__(self, doom_path, wad_path, pk3_path=None, saves_path=None, config_path=None):
        self._doom_path = doom_path
        self._wad_path = wad_path
        self._pk3_path = pk3_path
        self._saves_path = saves_path
        self._config_path = config_path

    def launch(self):
        launch_command = []

        if self._doom_path is not None:
            launch_command.append(str(self._doom_path))
        if self._wad_path is not None:
            launch_command.append(str(self._wad_path))

        print(' '.join(launch_command))
        os.system(' '.join(launch_command))
