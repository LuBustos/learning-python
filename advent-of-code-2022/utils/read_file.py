"""Module providing a function printing python version."""


def read_file(path):
    """Reading txt files"""
    with open(file=path, mode="r", encoding='UTF-8') as file_handle:
        content = file_handle.readlines()
        return content
