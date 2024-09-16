def format_file_size(size_in_bytes: int) -> str:
    """
    Format the file size in bytes to a human-readable format.
    :param size_in_bytes: The file size in bytes.
    :return: The human-readable file size.
    """
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"

    if size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"

    if size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / 1024 ** 2:.2f} MB"

    return f"{size_in_bytes / 1024 ** 3:.2f} GB"