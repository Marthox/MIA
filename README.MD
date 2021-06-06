# **MIA (Medical Image Anonymizer)**

MIA is a software that allows to anonymize medical images in DICOM format (.dcm) and convert them to NIFTI format (.nii).

## *Requirements*

The listed requirements can be installed with the command "pip install [package name]", make sure you have the latest version of pip installed.

You can upgrade pip using:

```python -m pip install --upgrade pip```

| Software | Instalation Command |
| --- | :-- |
|[dicognito](https://pypi.org/project/dicognito/)|```pip install dicognito```|
|[nibabel](https://pypi.org/project/nibabel/)|```pip install nibabel```|
|[itk](https://pypi.org/project/itk/)|```pip install itk```|
|[numpy](https://pypi.org/project/numpy/)|```pip install numpy```|
|[dicom-numpy](https://pypi.org/project/dicom-numpy/)|```pip install dicom-numpy```|
|[medio](https://pypi.org/project/medio/)|```pip install medio```|

## *How to run*

- Clone or download the repo.
- Enter to the folder
- Run the main.py file with the command:
  - ```python main.py [args]```

### ***Arguments***

| Argument | Function |
| --- | :-- |
| -h, --help | show a help message and exit |
|-dir, --directory | Path to the folder where the images are located, by default is ./|
|-out, --output | Path to the folder where the images are located, by default is ./output/|
|-ext --extension | The extension of medical images you are looking to anonimize, by default is .dcm|
|-C, --convert | Boolean value which defines if converts the images to nifti by default is False|
|-A, --anonymize | Boolean value which defines if anonymize the images or not by default is False |

### ***Examples***

#### **Anonymize**

Supose there is a folder aside the main.py file called "images" to anonymize these image you should run either:

- ```python main.py -A```
- ```python main.py --anonymize```

#### **Custon dir anonymize**

Supose there is a folder in your desktop (\~/usr/desktop/) called "images", which contains the images to anonymize, you should then run either:

- ```python main.py -dir "~/usr/desktop/images" -A```
- ```python main.py -dir "~/usr/desktop/images" --anonymize```

#### **Custom output dir anonymize**

Supose there is a folder in your desktop (\~/usr/desktop/) called "images", which contains the images to anonymize, and you want then to output in your documents (\~/usr/documents/), you should then run either:

- ```python main.py -dir "~/usr/desktop/images" -out "~/usr/documents/" -A```
- ```python main.py -dir "~/usr/desktop/images" -out "~/usr/documents/" --anonymize```

#### **Convert**

Supose there is a folder aside the main.py file called "images" to anonymize and convert these image you should run either:

- ```python main.py -A -C```
- ```python main.py --anonymize --convert```
