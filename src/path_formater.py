from os import path


def path_formater(parent_dirs, relative_dirs):
    full_dirs = []

    for directory in relative_dirs:
        splited_dir = directory.split(path.sep)
        splited_dir.insert(0, parent_dirs)
        output_dir = path.sep.join(splited_dir)
        full_dirs.append(output_dir)

    return full_dirs
