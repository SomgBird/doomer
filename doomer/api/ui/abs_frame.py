from abc import ABC, abstractmethod


class AbstractFrame(ABC):
    @abstractmethod
    def __init__(self, window, config, side):
        """
        Abstract frame constructor
        :param window: frame layout window
        :param config: Doomer config
        :param side: layout side
        """
        self._window = window
        self._config = config
        self._side = side
