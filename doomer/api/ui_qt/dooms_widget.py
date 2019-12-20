from PyQt5.QtWidgets import QFrame, QWidget, QVBoxLayout, QListWidget, QHBoxLayout, QPushButton, QFileDialog, \
    QErrorMessage, QLabel, QAbstractItemView

from doomer.api.dooms_handler import DoomsHandler
from doomer.api.config import Config


class DoomsWidget(QWidget):
    def __init__(
            self,
            config: Config,
            dooms_handler: DoomsHandler,
            name: str,
            dooms_key: str,
            *args,
            **kwargs
    ):
        # Dooms widget setup
        super(DoomsWidget, self).__init__(*args, **kwargs)

        self._config = config
        self._dooms_handler = dooms_handler
        self._name = name
        self._dooms_key = dooms_key
