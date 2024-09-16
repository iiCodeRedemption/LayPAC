import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog as fd

from config import config

from utils.file import read_content, get_file_size

from core.gui.base_gui_elem import BaseGUIElem

from core.gui.widgets.menubar import MenuBar

from core.gui.managers.panel_manager import PanelManager

from core.gui.panels.welcome_panel import WelcomePanel
from core.gui.panels.main_content_panel import MainContentPanel

from core.gui.dialogs.about_dialog import AboutDialog

class MainApplication(ttk.Frame, BaseGUIElem):
    def __init__(self, root: ThemedTk) -> None:
        super().__init__(root)

        self.root = root

        self._panel_manager = PanelManager(self)
        self._panel_manager.pack(fill="both", expand=True)

        self._welcome_panel = None
        self._main_content_panel = None

        self._menubar = None

        self.setup_ui()

    def setup_ui(self) -> None:
        self._menubar = MenuBar(self.root, self._open_file, self._show_about, self.root.quit)

        self._welcome_panel = WelcomePanel(self, self._panel_manager)
        self._main_content_panel = MainContentPanel(self, self._panel_manager)

        self._panel_manager.add_panel("welcome", self._welcome_panel)
        self._panel_manager.add_panel("main", self._main_content_panel)

        show_welcome = config.get_boolean("DEFAULT", "show_welcome", True)
        if show_welcome:
            self._menubar.disable()
            self._panel_manager.show_panel("welcome")
        else:
            self._menubar.enable()
            self._panel_manager.show_panel("main")

    def _open_file(self) -> None:
        filename = fd.askopenfilename(title="Open PAC File", filetypes=[("PAC files", "*.pac"), ("All files", "*")])

        if not filename:
            return

        file_details = {
            "path": filename,
            "content": read_content(filename),
            "size": get_file_size(filename)
        }

        self._main_content_panel.load_file_details(file_details)

    def _show_about(self) -> None:
        AboutDialog(self)

    @property
    def menubar(self) -> MenuBar:
        return self._menubar