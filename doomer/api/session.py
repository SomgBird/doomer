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

        self._wads_handler = None
        self.update_wads_handler()

        self._dooms_handler = DoomsHandler(self._config.config_dict['dooms_path'])
        # TODO: add other handlers

    def update_wads_handler(self, wads_path=None):
        if wads_path is None:
            self._wads_handler = WADsHandler(self._config.config_dict['wads_path'])
        else:
            self._wads_handler = WADsHandler(wads_path)
