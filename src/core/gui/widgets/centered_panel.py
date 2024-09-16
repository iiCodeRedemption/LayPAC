from tkinter import ttk

from core.gui.widgets.base_panel import BasePanel

class CenteredPanel(BasePanel):
    def __init__(self, parent: ttk.Widget) -> None:
        """
        Handy class to create a panel that is centered in the parent widget.
        :param parent: The parent widget.
        """
        super().__init__(parent)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.content_frame.grid(row=1, column=0)
