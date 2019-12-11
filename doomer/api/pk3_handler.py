from files_handler import FilesHandler


class PK3Handler(FilesHandler):
    @property
    def pk3_dict(self):
        """
        dict of all WADs files
        """
        return self._files_dict

    @property
    def pk3_path(self):
        """
        path to WADs directory
        """
        return self._files_path

    def __init__(self):
        """
        PK3Handler constructor
        """
        super().__init__(['pk3'])


