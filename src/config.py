import os
import configparser
from typing import Union

from constants import BASE_DIR, CONFIG_PATH

class Config:
    def __init__(self, config_path: str = CONFIG_PATH) -> None:
        """
        Class to manage the configuration of the application.
        :param config_path: A string representing the path to the configuration file.
        """
        self._config = configparser.ConfigParser()
        self._config_path = config_path

        self._load_config()

    def _load_config(self) -> None:
        """
        Load the configuration from the config file.
        :return: None
        """
        if not os.path.exists(self._config_path):
            self._set_default_config()
            self.save_config()
            return

        self._config.read(self._config_path)

    def _set_default_config(self) -> None:
        """
        Set the default configuration values.
        :return: None
        """
        self._config['DEFAULT'] = {
            "show_welcome": "true",
        }

    def get(self, section: str, option: str, fallback=None) -> Union[str, None]:
        """
        Get a configuration value.
        :param section: The section of the configuration.
        :param option: The option of the configuration.
        :param fallback: The fallback value if the option is not found.
        :return: None if the option is not found, otherwise a string representing the value.
        """
        return self._config.get(section, option, fallback=fallback)

    def get_int(self, section: str, option: str, fallback: int = 0) -> int:
        """
        Get a configuration value as an integer.
        :param section: The section of the configuration.
        :param option: The option of the configuration.
        :param fallback: The fallback value if the option is not found (default is 0).
        :return: The integer value of the option.
        """
        return self._config.getint(section, option, fallback=fallback)

    def get_boolean(self, section: str, option: str, fallback: bool = False) -> bool:
        """
        Get a configuration value as a boolean.
        :param section: The section of the configuration.
        :param option: The option of the configuration.
        :param fallback: The fallback value if the option is not found (default is False).
        :return: The boolean value of the option.
        """
        return self._config.getboolean(section, option, fallback=fallback)

    def set(self, section: str, option: str, value: Union[str, int, bool]) -> None:
        """
        Set a configuration value.
        :param section: The section of the configuration to set.
        :param option: The option of the configuration to set.
        :param value: The value to set the option to.
        :return: None
        """
        if section not in self._config:
            self._config.add_section(section)

        self._config.set(section, option, value)

    def save_config(self) -> None:
        """
        Save the configuration to the config file.
        :return: None
        """
        with open(self._config_path, "w") as configfile:
            self._config.write(configfile)

config = Config()