import os

def read_content(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()

def get_file_size(filepath: str) -> int:
    """
    Get the size of a file in bytes
    :param filepath: The path to the file
    :return: The size of the file in bytes
    """
    return os.path.getsize(filepath)