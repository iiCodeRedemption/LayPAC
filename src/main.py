from ttkthemes import ThemedTk

from constants import APP_TITLE, APP_THEME
from config import config

from core.main_application import MainApplication

from utils.gui import center_window

def main() -> None:
    root = ThemedTk(theme=APP_THEME)

    root.title(APP_TITLE)
    root.geometry("800x600")

    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)


    center_window(root)

    root.mainloop()

if __name__ == "__main__":
    main()
