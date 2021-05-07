from glob import glob
from os import path

'''
Function "path_formater" convert a arr of relative paths to a arr of full paths
    using a parent dir.

    Arguments:
        parent_dir: It is a string which indicates the path to a parent directory
        extension: It is a string which indicates the type of files the function
            is looking for
        index: It is an integer, that indicates the end of the parent path, once
            splited using the sistem separator
        
    Return: A parser object
'''
def recursive_folder_search(parent_dir, extension, index):
    items = glob(
        parent_dir + '/*[!env][!src]*',
        recursive=False
        )
    interest_folders = []

    for item in items:
        body, ext = path.splitext(item)

        if path.isdir(item):
            interest_folders = interest_folders + \
                                recursive_folder_search(item, extension, index)

        elif path.isfile(item) and ext == extension:
            folder = body.split(path.sep)
            del folder[-1]
            folder = path.sep.join(folder[index:])
            if folder not in interest_folders:
                interest_folders.append(folder)

    return interest_folders
