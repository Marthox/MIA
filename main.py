from os import getcwd, path

from src.recursive_folder_search import recursive_folder_search
from src.path_formater import path_formater
from src.anonymizer import anonymize
from src.input_parser import create_parser
from src.converter import convert


def main():
    # Define the default values
    ext = '.dcm'
    parent_dir = getcwd()
    output_dir = getcwd() + path.sep + 'output'

    index_to_relative = len(parent_dir.split(path.sep))

    default_arguments = {
        'ext': ext,
        'parent_dir': parent_dir,
        'output_dir': output_dir
    }

    parser = create_parser(default_arguments=default_arguments)

    # Obtain the args
    args = parser.parse_args()
    parser.print_help()

    relative_dirs_to_folders = recursive_folder_search(
        parent_dir=parent_dir, extension=ext, index=index_to_relative
    )

    full_dirs_to_outputs = path_formater(
        parent_dirs=output_dir, relative_dirs=relative_dirs_to_folders
    )

    full_dirs_to_folders = path_formater(
        parent_dirs=parent_dir, relative_dirs=relative_dirs_to_folders
    )

    if args.dir != None:
        parent_dir = args.dir
    
    if args.out != None:
        output_dir = args.out

    if args.aext != None:
        ext = args.aext

    if args.cext != None:
        ext = args.cext

    if args.A:
        anonymize(
            image_dirs=full_dirs_to_folders,
            output_dirs=full_dirs_to_outputs,
            extension=ext
        )

    if args.C:
        convert(
            image_dirs=full_dirs_to_folders,
            output_dirs=full_dirs_to_outputs,
            ext=ext
        )

if __name__ == '__main__':
    main()
