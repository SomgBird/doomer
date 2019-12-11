from files_handler import FilesHandler


class WADsHandler(FilesHandler):
    @property
    def wads_dict(self):
        """
        dict of all WADs files
        """
        return self._files_dict

    @property
    def wads_path(self):
        """
        path to WADs directory
        """
        return self._files_path

    def __init__(self):
        """
        WADsHandler constructor
        """
        super().__init__(['wad', 'WAD'])

