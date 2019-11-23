from pathlib import Path


class WADHandler:
    @property
    def get_wad_list(self):
        """
        :return: list of all WADs files
        """
        return self._wad_list

    @property
    def get_wad_path(self):
        """
        :return: WADs files directory path
        """
        return self._wad_path_str

    def __init__(self, wad_path: str):
        """

        :param wad_path:
        """
        self._wad_path_str = wad_path
        self._wad_path = Path(wad_path)

        pass
        # TODO: wad load
