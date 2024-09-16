import tkinter as tk
from tkinter import ttk

from utils.gui import center_window

from core.gui.base_gui_elem import BaseGUIElem

class BaseDialog(tk.Toplevel, BaseGUIElem):
    def __init__(
        self,
        parent: ttk.Widget,
        title: str = "Dialog",
        width: int = 400,
        height: int = 250,
        ok_button_text: str = "OK",
        ok_button_command: callable = None,
        cancel_button: bool = False,
        cancel_button_text: str = "Cancel",
        cancel_button_command: callable = None,
    ) -> None:
        super().__init__(parent)

        self._ok_button_text = ok_button_text
        self._ok_button_command = ok_button_command if ok_button_command else self.close

        self._cancel_button = cancel_button
        self._cancel_button_text = cancel_button_text
        self._cancel_button_command = cancel_button_command if cancel_button_command else self.close

        self.title(title)
        self.geometry(f"{width}x{height}")

        self.transient(parent)
        self.grab_set()

        self.body_frame = None
        self.button_frame = None

        self.setup_ui()
        self.focus_force()

        center_window(self)

    def setup_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.body_frame = ttk.Frame(self)
        self.body_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10)

        if self._cancel_button:
            cancel_button = ttk.Button(self.button_frame, text=self._cancel_button_text, command=self._cancel_button_command)
            cancel_button.pack(side="right")

        ok_button = ttk.Button(self.button_frame, text=self._ok_button_text, command=self._ok_button_command)
        ok_button.pack(side="right", padx=5)


    def close(self) -> None:
        """
        Close the dialog
        :return: None
        """
        self.destroy()
