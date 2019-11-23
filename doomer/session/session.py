from doomer.wads_handler import WADsHandler


class Session:
    @property
    def wads_handler(self):
        return self._wads_handler

    def __init__(self, wads_path_str: str, screenshots_path_str: str, pk3_path_str: str, saves_path_str: str):
        """
        Session constructor
        :param wads_path_str: WADs files directory path
        :type wads_path_str: str
        :param screenshots_path_str: screenshots directory path
        :type screenshots_path_str: str
        :param pk3_path_str: pk3 files directory path
        :type pk3_path_str: str
        :param saves_path_str: save files directory path
        :type saves_path_str: str
        """
        self._wads_handler = WADsHandler(wads_path_str)
        # TODO: add other handlers
