from doomer.api.wads_handler import WADsHandler
from pathlib import Path


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    def __init__(self, wads_path, screenshots_path, pk3_path, saves_path):
        """
        Session constructor
        :param wads_path: WADs files directory path
        :param screenshots_path: screenshots directory path
        :param pk3_path: pk3 files directory path
        :param saves_path: save files directory path
        """
        self._wads_handler = WADsHandler(Path(wads_path))
        # TODO: add other handlers
