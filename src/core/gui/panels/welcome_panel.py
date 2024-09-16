import tkinter as tk
from tkinter import ttk

from constants import APP_TITLE, APP_DESCRIPTION, FONT_FAMILY
from config import config

from utils.gui import toggle_menubar

from core.gui.managers.panel_manager import PanelManager

from core.gui.widgets.centered_panel import CenteredPanel

class WelcomePanel(CenteredPanel):
    def __init__(self, parent: ttk.Widget, panel_manager: PanelManager) -> None:
        """
        The welcome panel that is shown when the application is started.
        :param parent: The parent widget.
        :param panel_manager: The panel manager instance.
        """
        super().__init__(parent)

        self._panel_manager = panel_manager
        self._show_welcome_var = tk.BooleanVar(value=config.get_boolean("DEFAULT", "show_welcome", fallback=True))

        self._show_welcome_checkbox = None

        self.setup_ui()

    def setup_ui(self) -> None:
        title_label = ttk.Label(self.content_frame, text=f"Welcome to {APP_TITLE}", font=(FONT_FAMILY, 20, "bold"))
        title_label.pack(pady=(20, 10))

        description_label = ttk.Label(
            self.content_frame,
            text=APP_DESCRIPTION,
            wraplength=500,
            justify="center"
        )
        description_label.pack(pady=(10, 10))

        grey_description_label = ttk.Label(
            self.content_frame,
            text="Created with love by iiCodeRedemption (MrSevyu).",
            font=(FONT_FAMILY, 10),
            foreground="grey",
            justify="center"
        )
        grey_description_label.pack(pady=(0, 20))

        self._show_welcome_checkbox = ttk.Checkbutton(
            self.content_frame,
            text="Show this screen on startup",
            variable=self._show_welcome_var,
            command=self._toggle_show_welcome
        )
        self._show_welcome_checkbox.pack(pady=(0, 20))

        continue_button = ttk.Button(self.content_frame, text="Continue", command=self._on_continue_clicked)
        continue_button.pack(pady=(20, 0))

    def _toggle_show_welcome(self):
        config.set("DEFAULT", "show_welcome", str(self._show_welcome_var.get()).lower())
        config.save_config()

    def _on_continue_clicked(self):
        self.parent.menubar.enable()
        self._panel_manager.show_panel("main")
