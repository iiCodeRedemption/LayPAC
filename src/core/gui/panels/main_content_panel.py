import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.gui.widgets.base_panel import BasePanel

from core.gui.managers.panel_manager import PanelManager
from core.gui.managers.tab_manager import TabManager

from core.gui.tabs.file_details_tab import FileDetailsTab
from core.gui.tabs.file_content_tab import FileContentTab
from core.gui.tabs.file_output_tab import FileOutputTab

from core.pac.pac_parser import PacParser
from exceptions.pac_parser_exception import PacParserException

class MainContentPanel(BasePanel):
    def __init__(self, parent: ttk.Widget, panel_manager: PanelManager) -> None:
        """
        This class represents the main content panel of the application.
        :param parent: The parent widget.
        :param panel_manager: The panel manager instance.
        """
        super().__init__(parent)

        self._panel_manager = panel_manager

        self._tab_manager = None

        self._file_details = {}

        self._file_details_tab = None
        self._file_content_tab = None
        self._file_output_tab = None

        self._parse_button = None
        self._input_entry_url = None
        self._input_entry_host = None

        self.setup_ui()

    def setup_ui(self) -> None:
        self._tab_manager = TabManager(self.content_frame)
        self._tab_manager.pack(fill="both", expand=True)

        self._file_details_tab = FileDetailsTab(self._tab_manager)
        self._file_content_tab = FileContentTab(self._tab_manager)
        self._file_output_tab = FileOutputTab(self._tab_manager)

        self._tab_manager.add_tab(tab_id="file_details", tab_instance=self._file_details_tab)
        self._tab_manager.add_tab(tab_id="content", tab_instance=self._file_content_tab)
        self._tab_manager.add_tab(tab_id="output", tab_instance=self._file_output_tab)

        bottom_frame = ttk.Frame(self.content_frame)
        bottom_frame.pack(fill="x", pady=10, padx=10)

        url_label = ttk.Label(bottom_frame, text="URL:")
        url_label.pack(side="left", padx=(0, 10))

        self._input_entry_url = ttk.Entry(bottom_frame)
        self._input_entry_url.pack(side="left", fill="x", expand=True)

        host_label = ttk.Label(bottom_frame, text="Host:")
        host_label.pack(side="left", padx=(10, 10))

        self._input_entry_host = ttk.Entry(bottom_frame)
        self._input_entry_host.pack(side="left", fill="x", expand=True)

        self._parse_button = ttk.Button(bottom_frame, text="Parse", command=self._parse_content)
        self._parse_button.pack(side="right", padx=(10, 0))

        description = ttk.Label(self.content_frame, text="If the URL is not provided, the host will be used to parse"
                                                         " the PAC file, and vice versa. Otherwise, both the URL and"
                                                         " host will be used.")
        description.config(foreground="gray", wraplength=500, justify="center")
        description.pack(side="bottom", pady=(0, 10))

    def load_file_details(self, file_details: dict) -> None:
        """
        This method is used to load the file details into the main content panel.
        :param file_details: The file details dictionary obtained when the user selects a file.
        :return: None
        """
        self._file_details = file_details

        self._file_details_tab.update_content(self._file_details)

        if self._file_details:
            self._file_content_tab.update_content(self._file_details["content"])
        else:
            self._file_content_tab.update_content(self._file_content_tab.content)

        self._input_entry_url.config(state="normal")
        self._parse_button.config(state="normal")

    def _parse_content(self) -> None:
        """
        This method is used to parse the user input and display the output.
        Calls the PacParser class to parse the user input.
        :return: None
        """
        url = self._input_entry_url.get()
        host = self._input_entry_host.get()

        if not url and not host:
            messagebox.showwarning("Input Error", "Please enter a URL or host to parse the PAC file.")
            return

        try:
            parsed_output = PacParser.parse(self._file_content_tab.content, url, host)
            self._file_output_tab.update_content(parsed_output)
            self._tab_manager.show_tab("output")
        except PacParserException as e:
            messagebox.showerror("PAC Parsing Error", f"Failed to parse the input: {str(e)}")
        finally:
            self._input_entry_url.delete(0, tk.END)
            self._input_entry_host.delete(0, tk.END)
