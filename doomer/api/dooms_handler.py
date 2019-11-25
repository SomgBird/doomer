class DoomsHandler:
    @property
    def dooms(self):
        return self._dooms

    def __init__(self, config):
        """
        DoomsHandler constructor
        :param config: doomer configuration
        """
        self._config = config
        self._dooms = config['dooms']

    def add_doom(self, path, name: str):
        """
        Add new Doom port to doomer
        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        self._dooms[name] = path
        self._config.update_dooms(self._dooms)

    def delete_doom(self, name: str):
        """
        Delete Doom port from doomer
        :param name: Doom port name
        :return: None
        """
        self._dooms.pop(name, None)
        self._config.update_dooms(self._dooms)

