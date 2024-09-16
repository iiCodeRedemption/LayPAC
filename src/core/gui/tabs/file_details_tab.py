from tkinter import ttk

from utils.formatters import format_file_size

from core.gui.widgets.base_tab import BaseTab

class FileDetailsTab(BaseTab[dict]):
    def __init__(self, parent: ttk.Widget) -> None:
        super().__init__(parent=parent, tab_title="PAC File Details", content_title="File Details")

        self._details_label = None

        self.setup_ui()

    def setup_ui(self) -> None:
        super().setup_ui()

        self._details_label = ttk.Label(self.content_frame, text="No file selected")
        self._details_label.pack(anchor="w")

    def update_content(self, file_details: dict) -> None:
        content = file_details["content"]
        file_path = file_details["path"]
        size = file_details["size"]

        total_lines = len(content.splitlines())

        details = (
            f"File Path: {file_path}\n"
            f"File Size: {format_file_size(size)}\n"
            f"Total Lines: {total_lines}"
        )
        self._details_label.config(text=details)
