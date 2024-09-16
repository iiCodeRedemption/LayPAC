from typing import Generic, TypeVar
from tkinter import ttk

from core.gui.widgets.base_panel import BasePanel

T = TypeVar("T")

class BaseTab(BasePanel, Generic[T]):
    def __init__(
        self,
        parent: ttk.Widget,
        tab_title: str = "Tab",
        content_title: str = "Content"
    ) -> None:
        super().__init__(parent)

        self.title = tab_title
        self.content_title = content_title

        self.content_frame.pack_configure(padx=10)

    def setup_ui(self) -> None:
        label = ttk.Label(self.content_frame)
        label.pack(anchor="w", pady=10)

    def update_content(self, value: T) -> None:
        pass

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")

        self._title = title or "Tab"

    @property
    def content_title(self) -> str:
        return self._content_title

    @content_title.setter
    def content_title(self, content_title: str) -> None:
        if not isinstance(content_title, str):
            raise ValueError("Content title must be a string.")

        new_content_title = content_title or "Content"

        self._content_title = new_content_title