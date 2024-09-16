import tkinter as tk
from tkinter import ttk

from core.gui.base_gui_elem import BaseGUIElem

class BasePanel(ttk.Frame, BaseGUIElem):
    def __init__(self, parent: ttk.Widget) -> None:
        super().__init__(parent)

        self.parent = parent

        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(fill="both", expand=True, anchor="w")