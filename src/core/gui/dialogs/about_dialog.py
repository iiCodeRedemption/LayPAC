from tkinter import ttk

from constants import APP_TITLE, FONT_FAMILY, FONT_SIZE
from utils.gui import center_window

from core.gui.dialogs.base_dialog import BaseDialog

class AboutDialog(BaseDialog):
    def __init__(self, parent: ttk.Widget) -> None:
        super().__init__(parent, title="About LayPAC")

        self.setup_ui()

    def setup_ui(self) -> None:
        super().setup_ui()

        title_label = ttk.Label(self.body_frame, text=APP_TITLE, font=(FONT_FAMILY, 20, "bold"))
        title_label.pack(pady=10)

        details_label = ttk.Label(
            self.body_frame,
            text="Developed by iiCodeRedemption (MrSevyu).\nContact me at: javiermdeb@gmail.com.",
            justify="center",
        )
        details_label.pack(pady=10)
