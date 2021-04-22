from os import getcwd, path
from argparse import ArgumentParser

from src.recursive_folder_search import recursive_folder_search
from src.path_formater import path_formater


def main():
    # Define the default values
    default_ext = ''
    parent_dir = getcwd()
    output_dir = getcwd() + path.sep + 'output'

    index_to_relative = len(parent_dir.split(path.sep))

    # Create the parser
    parser = ArgumentParser(
        allow_abbrev=False,
        prog='Anonimizer',
        usage='%(prog)s argument value',
        epilog='Execution completed!',
        description='Anonimization script for medical imaging'
        )

    # Add the arguments
    parser.add_argument(
        '-dir', '--directory', type=str, action='store',
        help='Path to the folder where the images are '
             'located (default:[.{}])'.format(
                                 path.sep
                                )
        )
    parser.add_argument(
        '-out', '--output', type=str, action='store',
        help='Path to the folder where the images are '
             'located (default:[.{}])'.format(
                                 path.sep
                                )
        )
    parser.add_argument(
        '-ext', '--extension', type=str, action='store',
        help='the extension of medical images you are '
             'looking to anonimize (default:["{}"])'.format(
                                 default_ext
                                )
        )

    # Obtain the args
    args = parser.parse_args()
    parser.print_help()

    relative_dirs_to_folders = recursive_folder_search(
        parent_dir=parent_dir, extension=default_ext, index=index_to_relative
        )

    full_dirs_to_outputs = path_formater(
        parent_dir=output_dir, relative_dirs=relative_dirs_to_folders
        )

    full_dirs_to_folders = path_formater(
        parent_dir=parent_dir, relative_dirs=relative_dirs_to_folders
        )


if __name__ == '__main__':
    main()
