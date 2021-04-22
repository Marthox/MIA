from glob import glob
from pydicom import dcmread
from json import dumps
from dicognito import anonymizer as dicognito_anonymizer

anonymizer = dicognito_anonymizer.Anonymizer()


def anonymize(image_dirs, output_dirs, extension):
    traceback = {}
    for folder in image_dirs:
        items = glob(folder + '/*'+extension, recursive=False)
        for image in items:
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

    json_data = dumps(traceback)
    f = open('traceback.json', 'w')
    f.write(json_data)
    f.close()

    for image in traceback:
        print(image)

    return(traceback)
