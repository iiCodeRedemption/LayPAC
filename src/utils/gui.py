from typing import Union

import tkinter as tk
from tkinter import ttk

def center_window(root: tk.Tk) -> None:
    root.update_idletasks()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    x = screen_width // 2 - window_width // 2
    y = screen_height // 2 - window_height // 2

    root.geometry(f"+{x}+{y}")

def toggle_menubar(menubar: tk.Menu, enabled: bool = True) -> None:
    menu_items = menubar.winfo_children()
    for index, menu_item in enumerate(menu_items, start=1):
        menubar.entryconfig(index, state="normal" if enabled else "disabled")