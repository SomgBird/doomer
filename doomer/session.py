from pathlib import Path
from doomer.api.wads_handler import WADsHandler
from doomer.api.dooms_handler import DoomsHandler


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    @property
    def dooms_handler(self):
        return self._dooms_handler

    def __init__(self, config, wads_path, screenshots_path, pk3_path, saves_path):
        """
        Session constructor
        :param wads_path: WADs files directory path
        :param screenshots_path: screenshots directory path
        :param pk3_path: pk3 files directory path
        :param saves_path: save files directory path
        """
        self._wads_handler = WADsHandler(Path(wads_path))
        self._dooms_handler = DoomsHandler()
        # TODO: add other handlers

