from os import makedirs, path
from medio import read_img, save_img


def convert(image_dirs, output_dirs, ext):
    for index in range(len(image_dirs)):
        try:
            print(image_dirs[index])
            array, metadata = read_img(image_dirs[index], backend='pdcm')
            folder_name = output_dirs[index].split(path.sep)[-1].split(' ')[0]
            makedirs(output_dirs[index])
            save_img(
                output_dirs[index] + path.sep + folder_name + ext,
                array, metadata, backend='nib'
            )
        except Exception as err:
            print(err)
            problematic_folder = image_dirs[index]
            print('Error converting images at {}'.format(problematic_folder))
            break
    return 0
