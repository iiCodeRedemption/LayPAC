import tkinter as tk
from tkinter import ttk

from core.gui.widgets.base_panel import BasePanel

class PanelManager(tk.Frame):
    def __init__(self, parent: ttk.Widget) -> None:
        """
        Takes care of managing panels in the application.
        :param parent: The parent widget.
        """
        super().__init__(parent)

        self.panels = {}

    def add_panel(self, panel_name: str, panel_frame: BasePanel) -> None:
        """
        Adds a panel to the manager.
        :param panel_name: The name of the panel.
        :param panel_frame: The panel frame.
        :return: None
        """
        self.panels[panel_name] = panel_frame
        panel_frame.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

    def show_panel(self, panel_name: str) -> None:
        """
        Gets a panel by name and raises it.
        :param panel_name: The name of the panel.
        :return: None
        """
        panel: BasePanel = self.panels.get(panel_name)

        if not panel:
            return

        panel.tkraise()