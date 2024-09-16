import tkinter as tk
from tkinter import ttk

from core.gui.widgets.base_tab import BaseTab

class TabManager(ttk.Notebook):
    def __init__(self, parent: ttk.Widget) -> None:
        """
        Tab manager class to manage tabs in the application.
        :param parent: The parent widget.
        """
        super().__init__(parent)

        self._tabs = {}

    def add_tab(self, tab_id: str, tab_instance: BaseTab) -> None:
        """
        Add a tab to the tab manager.
        :param tab_id: The tab id.
        :param tab_instance: The tab instance.
        :return: None
        """
        self._tabs[tab_id] = tab_instance
        self.add(tab_instance, text=tab_instance.title)

    def show_tab(self, tab_id: str) -> None:
        """
        Show a tab by its id.
        :param tab_id: The tab id.
        :return: None
        """
        if tab_id not in self._tabs:
            return

        self.select(self._tabs[tab_id])
