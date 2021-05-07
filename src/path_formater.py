from os import path

'''
Function "path_formater" convert a arr of relative paths to a arr of full paths
    using a parent dir.

    Arguments:
        parent_dir: It is a string which indicates the path to a parent directory
        relative_dirs: It is an array that contains realative dirs to concat 
            to the parent_dir
        
    Return: A parser object
'''
def path_formater(parent_dir, relative_dirs):
    full_dirs = []

    for directory in relative_dirs:
        splited_dir = directory.split(path.sep)
        splited_dir.insert(0, parent_dir)
        output_dir = path.sep.join(splited_dir)
        full_dirs.append(output_dir)

    return full_dirs
