from glob import glob
from pydicom import dcmread
from dicognito import anonymizer as dicognito_anonymizer

anonymizer = dicognito_anonymizer.Anonymizer()


def anonymize(image_dirs, output_dirs, extension):
    trace_back = {}
    for folder in image_dirs:
        items = glob(folder + '/*'+extension, recursive=False)
        for image in items:
            with dcmread(image) as dataset:
                print(dataset[0x0010, 0x0020])
                break
                anonymizer.anonymize(dataset)
                dataset.save_as(image)
