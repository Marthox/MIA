from argparse import ArgumentParser

'''
Function "create_parser" creates a parser to interpret user inputs.

    Arguments:
        default_arguments: It is a dictionary that receives as key, 
            the name of the argument, and as value, the default value that 
            the argument will take in case it is not specified by the user.

    Return: A parser object
'''
def create_parser(default_arguments):
    # Creating the parser
    parser = ArgumentParser(
        allow_abbrev=False,
        prog='Anonimizer',
        usage='%(prog)s argument value',
        epilog='Execution completed!',
        description='Anonimization script for medical imaging'
    )

    # Add the arguments
    parser.add_argument(
        '-dir', type=str, action='store',
        help='Path to the folder where the images are '
             'located (default:[{}])'.format(
                                 default_arguments['parent_dir']
                                )
    )
    parser.add_argument(
        '-out', type=str, action='store',
        help='Path to the folder where the images are '
             'located (default:[{}])'.format(
                                 default_arguments['output_dir']
                                )
    )
    parser.add_argument(
        '-aext', action='store',
        help='The extension of medical images you are '
             'looking to anonimize (default:[{}])'.format(
                                 default_arguments['ext']
                                )
    )
    parser.add_argument(
        '-cext', action='store',
        help='The extension of medical images you are '
             'looking to anonimize (default:[{}])'.format(
                                 default_arguments['ext']
                                )
    )
    parser.add_argument(
        '-C', action='store_true',
        help='Boolean value  which defines if converts '
             'the images to nifti (default:[False])'
    )
    parser.add_argument(
        '-A', action='store_true',
        help='Boolean value  which defines if anonymize '
             'the images or not (default:[False])'
    )

    return parser
