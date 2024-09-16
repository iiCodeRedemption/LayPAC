import tkinter as tk
from tkinter import ttk

from utils.file import read_content, get_file_size
from utils.formatters import format_file_size

from core.gui.widgets.base_tab import BaseTab

class FileContentTab(BaseTab[str]):
    def __init__(self, parent: ttk.Widget) -> None:
        super().__init__(parent=parent, tab_title="PAC File Content", content_title="File Content")

        self._content_text = None

        self.setup_ui()

    def setup_ui(self) -> None:
        super().setup_ui()

        text_frame = ttk.Frame(self.content_frame)
        text_frame.pack(fill="both", expand=True)

        self._content_text = tk.Text(text_frame, wrap="none", height=15)
        self._content_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self._content_text.yview)
        scrollbar.pack(side="right", fill="y")

        self._content_text.config(yscrollcommand=scrollbar.set)

    def update_content(self, content: str) -> None:
        self._content_text.config(state="normal")

        self._content_text.delete(1.0, tk.END)
        self._content_text.insert(tk.END, content)
        self._content_text.yview_moveto(0)

    @property
    def content(self) -> str:
        return self._content_text.get(1.0, tk.END)
