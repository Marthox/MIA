from glob import glob
from pydicom import dcmread
from json import dumps
from dicognito import anonymizer as dicognito_anonymizer

'''
Function "anonymize" anonymize the images and write a traceback file which
    indicates the previous values of the anonymized images, this could be used
    in some scenarios but we strongly recomend to delete it.

    Arguments:
        image_dirs: It is an array which contains the folder directories
            of the dicom files

        output_dirs: It is an array which contains the folder directories
            to output the converted files
            
        extension: It is a string which indicates the extension of the 
            images to convert
'''
def anonymize(image_dirs, output_dirs, extension):
    anonymizer = dicognito_anonymizer.Anonymizer()
    traceback = {}
    for folder in image_dirs:
        print('\nChecking folder: {}'.format(folder))
        items = glob(folder + '/*'+extension, recursive=False)
        for image in items:
            try:
                with dcmread(image) as dataset:
                    user_id = dataset[0x0010, 0x0020].value
                    image_id = dataset[0x0020, 0x0010].value

                    if user_id not in traceback:
                        traceback[user_id] = {'images': [image_id]}
                    else:
                        if 'images' not in traceback[user_id]:
                            traceback[user_id]['images'] = [image_id]
                        elif image_id not in traceback[user_id]['images']:
                            traceback[user_id]['images'].append(image_id)

                    anonymizer.anonymize(dataset)
                    dataset.save_as(image)

                    with dcmread(image) as anonymized_dataset:
                        anonymized_user_id = \
                            anonymized_dataset[0x0010, 0x0020].value
                        anonymized_image_id = \
                            anonymized_dataset[0x0020, 0x0010].value

                        if 'anonymized_user_id' not in \
                        traceback[user_id]:

                            traceback[user_id]['anonymized_user_id'] =\
                                anonymized_user_id

                        if 'anonymized_images' not in traceback[user_id]:
                            traceback[user_id]['anonymized_images'] = \
                                [anonymized_image_id]

                        elif anonymized_image_id not in \
                                traceback[user_id]['anonymized_images']:

                            traceback[user_id]['anonymized_images'].\
                                append(anonymized_image_id)

                    if 'protocol_name' not in traceback[user_id]:
                        traceback[user_id]['protocol_name'] = \
                            anonymized_dataset[0x0018, 0x1030].value

            except Exception as err:
                print("Error reading the file \n{}".format(image))
                print(err)

        print('Folder \n{}\n successfuly anonimized'.format(folder))

    json_data = dumps(traceback)
    f = open('traceback.json', 'w')
    f.write(json_data)
    f.close()
