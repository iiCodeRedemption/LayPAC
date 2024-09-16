from typing import Union

from pypac.parser import PACFile

from exceptions.pac_parser_exception import PacParserException

class PacParser:
    @staticmethod
    def parse(file_content: str, url: str, host: str = "") -> str:
        """
        Parse the PAC file content and return the proxy string using PyPAC.
        :param file_content: The content of the PAC file.
        :param url: The URL to be checked against the PAC file.
        :param host: The host to be checked against the PAC file (optional).
        :return: The proxy string for the provided URL.
        """
        try:
            pac = PACFile(file_content)
            proxy = pac.find_proxy_for_url(url, host)

            if not proxy:
                raise PacParserException("No proxy found for the given URL.")

            return proxy
        except Exception as e:
            raise PacParserException(f"PAC parsing error: {str(e)}") from e
