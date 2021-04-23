from os import makedirs, path
from medio import read_img, save_img


def convert(image_dirs, output_dirs):
    for index in range(len(image_dirs)):
        print('Loading Data')
        array, metadata = read_img(image_dirs[index], backend='itk')
        print('Data Loaded')
        folder_name = output_dirs[index].split(path.sep)[-1].split(' ')[0]
        print('Creating Output folder')
        makedirs(output_dirs[index])
        print('Saving the images')
        save_img(
            output_dirs[index] + path.sep + folder_name,
            array, metadata, backend='nib'
        )
    return 0
