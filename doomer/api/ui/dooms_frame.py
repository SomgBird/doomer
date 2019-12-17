import json
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.simpledialog

from pathlib import Path

from doomer.api.ui.abs_frame import AbstractFrame


class DoomsFrame(AbstractFrame):
    @property
    def active_doom(self):
        """
        :return: chosen Doom port
        """
        if len(self._dooms_list_box.curselection()) != 0:
            return self._dooms_list_box.get(self._dooms_list_box.curselection())
        return None

    @property
    def active_doom_path(self):
        """
        :return: chosen Doom port
        """
        active = self._dooms_handler.dooms_dict.get(self._dooms_list_box.get(tk.ACTIVE), None)
        if active is not None:
            return Path(active)
        return None

    def __init__(self, window, config, side, dooms_handler):
        """
        Dooms frame constructor
        :param window: frame layout window
        :param config: Doomer config
        :param side: layout side
        """
        super().__init__(window, config, side)
        self._dooms_handler = dooms_handler

        # Dooms management frame
        self._dooms_frame = tk.LabelFrame(self._window, text='Dooms')
        self._dooms_frame.pack(padx=10, pady=10, side=self._side)

        # Buttons subframe
        self._buttons_subframe = tk.Frame(self._dooms_frame)
        self._buttons_subframe.pack(side=tk.TOP)

        # Add Doom button
        self._add_dooms_button = tk.Button(self._buttons_subframe,
                                           text='Add',
                                           command=self.__add_doom_dialog)
        self._add_dooms_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Delete Doom button
        self._delete_doom_button = tk.Button(self._buttons_subframe,
                                             text='Delete',
                                             command=self.__delete_doom_dialog)
        self._delete_doom_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # List of Dooms
        self._dooms_list_box = tk.Listbox(
            self._dooms_frame,
            width=40,
            height=25,
            selectmode=tk.SINGLE,
            exportselection=False
        )
        self._dooms_list_box.pack()

    def __add_doom_dialog(self):
        """
        Add new Doom port from file system
        :return: None
        """
        doom_path = tk.filedialog.askopenfilename()
        if doom_path == '':
            return

        doom_name = tk.simpledialog.askstring('test', 'test')
        if doom_name is None:
            return

        self._dooms_handler.add_doom(name=doom_name, path=doom_path)
        self._dooms_handler.write_dooms(self._config.config_dict['dooms_path'])
        self.update_dooms_list_box()

    def __delete_doom_dialog(self):
        """
        Delete Doom port from Doomer
        :return: None
        """
        if tk.messagebox.askquestion('Sure?',
                                     'Are you really want to delete ' + str(self.active_doom) + ' from Doomer?') \
                != 'yes':
            return
        self._dooms_handler.delete_doom(self.active_doom)
        self._dooms_handler.write_dooms(self._config.config_dict['dooms_path'])
        self.update_dooms_list_box()

    def update_dooms_list_box(self):
        """
        Update list of Doom ports
        :return: None
        """
        try:
            self._dooms_handler.read_dooms(self._config.config_dict['dooms_path'])
        except FileNotFoundError:
            tk.messagebox.showerror('Path error!', self._config.config_dict['dooms_path'] + ' was not found!')
        except json.JSONDecodeError:
            tk.messagebox.showerror('Error!', self._config.config_dict['dooms_path'] + ' is corrupted!')

        self._dooms_list_box.delete(0, tk.END)
        for doom_name in self._dooms_handler.dooms_dict.keys():
            self._dooms_list_box.insert(0, doom_name)
