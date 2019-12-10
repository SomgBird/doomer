from wads_handler import WADsHandler
from dooms_handler import DoomsHandler
from config import Config


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    @property
    def dooms_handler(self):
        return self._dooms_handler

    @property
    def config(self):
        return self._config

    def __init__(self):
        """
        Session constructor
        """
        self._config = Config()
        self._wads_handler = WADsHandler()
        self._dooms_handler = DoomsHandler()
        # TODO: add other handlers
