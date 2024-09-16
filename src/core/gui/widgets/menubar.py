import tkinter as tk
from ttkthemes import ThemedTk

from core.gui.base_gui_elem import BaseGUIElem

from utils.gui import toggle_menubar

class MenuBar(tk.Menu, BaseGUIElem):
    def __init__(
        self,
        root: ThemedTk,
        on_open_file: callable,
        on_show_about: callable,
        on_exit: callable
    ) -> None:
        """
        This class represents the menubar of the application.
        :param root: The root window of the application.
        :param on_open_file: A callable that will be called when the user wants to open a file.
        :param on_show_about: A callable that will be called when the user wants to see the about dialog.
        :param on_exit: A callable that will be called when the user wants to exit the application.
        """
        super().__init__(root)

        self._root = root

        self._on_open_file = on_open_file
        self._on_exit = on_exit
        self._on_show_about = on_show_about

        self._menubar = None

        self.setup_ui()

    def setup_ui(self) -> None:
        self._menubar = tk.Menu(self._root)

        filemenu = tk.Menu(self._menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self._on_open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._on_exit)

        self._menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(self._menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self._on_show_about)
        self._menubar.add_cascade(label="Help", menu=helpmenu)

        self._root.config(menu=self._menubar)

    def enable(self) -> None:
        """
        Enable the menubar.
        :return: None
        """
        toggle_menubar(self._menubar, True)

    def disable(self) -> None:
        """
        Disable the menubar.
        :return: None
        """
        toggle_menubar(self._menubar, False)
