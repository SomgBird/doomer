from files_handler import FilesHandler


class PK3Handler(FilesHandler):
    def __init__(self):
        """
        PK3Handler constructor
        """
        super().__init__(['pk3'])


