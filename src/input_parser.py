from argparse import ArgumentParser


def create_parser(default_arguments):
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
             'located (default:[{}])'.format(
                                 default_arguments['parent_dir']
                                )
        )
    parser.add_argument(
        '-out', '--output', type=str, action='store',
        help='Path to the folder where the images are '
             'located (default:[{}])'.format(
                                 default_arguments['output_dir']
                                )
        )
    parser.add_argument(
        '-ext', '--extension', type=str, action='store',
        help='The extension of medical images you are '
             'looking to anonimize (default:[{}])'.format(
                                 default_arguments['ext']
                                )
        )
    parser.add_argument(
        '-C', '--convert', action='store_true',
        help='Boolean value  which defines if converts'
             'the images to nifti (default:[True])'
        )

    return parser
