from doomer.api.wads_handler import WADsHandler
from doomer.api.dooms_handler import DoomsHandler
from doomer.config import Config


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    @property
    def dooms_handler(self):
        return self._dooms_handler

    def __init__(self):
        """
        Session constructor
        """
        self._config = Config()
        self._wads_handler = WADsHandler(self._config.config_dict['wads_path'])
        self._dooms_handler = DoomsHandler(self._config.config_dict['dooms_path'])
        # TODO: add other handlers
