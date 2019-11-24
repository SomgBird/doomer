class DoomsHandler:
    @property
    def dooms(self):
        return self._dooms

    def __init__(self):
        self._dooms = None
        # TODO: load Doom ports locations

    def add_doom(self, path, name: str):
        """

        :param path: path to Doom port like GZDOOM, ZDOOM etc.
        :param name: name will be shown in Doom ports list
        :return: None
        """
        pass
        # TODO: add Doom ports