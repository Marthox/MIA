from glob import glob
from os import rename, getcwd, path


def add_extension(extension, file_path):
    root = getcwd()
    if not path.isfile(file_path):
        continue

    body, ext = path.splitext(file)
    if ext:
        src = path.join(root, file_path)
        dst = path.join(root, body + extension)
    else:
        src = path.join(root, file_path)
        dst = path.join(root, file_path + extension)
