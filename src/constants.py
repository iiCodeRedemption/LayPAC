import os
from typing import Literal

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, "config.ini")

# App
APP_TITLE = "LayPAC"
APP_DESCRIPTION = "Simple and easy to use GUI for working with Proxy Auto-Configuration (PAC) files."
APP_THEME = "breeze"

# UI
FONT_FAMILY = "Arial"
FONT_SIZE = 12