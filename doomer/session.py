from doomer.api.wads_handler import WADsHandler
from doomer.api.dooms_handler import DoomsHandler


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    @property
    def dooms_handler(self):
        return self._dooms_handler

    def __init__(self, config):
        """
        Session constructor
        :param config: doomer configuration
        """
        self._wads_handler = WADsHandler(config)
        self._dooms_handler = DoomsHandler(config)
        # TODO: add other handlers

