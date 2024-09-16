import tkinter as tk
from tkinter import ttk

from utils.file import read_content, get_file_size
from utils.formatters import format_file_size

from core.gui.widgets.base_tab import BaseTab

class FileOutputTab(BaseTab[str]):
    def __init__(self, parent: ttk.Widget) -> None:
        super().__init__(parent=parent, tab_title="PAC Output", content_title="Output")

        self._content_text = None

        self.setup_ui()

    def setup_ui(self) -> None:
        super().setup_ui()

        text_frame = ttk.Frame(self.content_frame)
        text_frame.pack(fill="both", expand=True)

        self._content_text = tk.Text(text_frame, wrap="none", height=15)
        self._content_text.pack(side="left", fill="both", expand=True)
        self._content_text.insert(tk.END, "No output available")
        self._content_text.config(state="disabled")

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self._content_text.yview)
        scrollbar.pack(side="right", fill="y")

        self._content_text.config(yscrollcommand=scrollbar.set)

    def update_content(self, pac_output: str) -> None:
        self._content_text.config(state="normal")

        self._content_text.delete(1.0, tk.END)
        self._content_text.insert(tk.END, pac_output)
        self._content_text.yview_moveto(0)

        self._content_text.config(state="disabled")
