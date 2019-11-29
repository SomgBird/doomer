from abc import ABC, abstractmethod


class AbstractFrame(ABC):
    @abstractmethod
    def __init__(self, window, session, side):
        """
        Abstract frame constructor
        :param window: frame layout window
        :param session: Doomer session
        :param side: layout side
        """
        self._window = window
        self._session = session
        self._side = side
