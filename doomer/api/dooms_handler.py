class DoomsHandler:
    @property
    def dooms(self):
        return self._dooms

    def __init__(self, config):
        """
        DoomsHandler constructor
        :param config: doomer configuration
        """
        self._dooms = config['dooms']

    def add_doom(self, path, name: str):
        """
        Add new Doom port to doomer
        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        pass
        # TODO: add Doom ports
