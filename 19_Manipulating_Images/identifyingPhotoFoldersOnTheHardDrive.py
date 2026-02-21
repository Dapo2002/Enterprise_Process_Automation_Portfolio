#! python3
# Scans the hard drive to find folders where the majority of files are large images.

import os
from PIL import Image

for foldername, subfolders, filenames in os.walk("C:\\"):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:

        # Check if file extension isn't .png or .jpg.
        extensions = ('.png', '.jpg')
        if not filename.lower().endswith(extensions):
            numNonPhotoFiles += 1
            continue  # skip to next filename

        # Open image file using Pillow.
        fullPath = os.path.join(foldername, filename)
        try:
            imageObj = Image.open(fullPath)
        except (FileNotFoundError, OSError, Image.DecompressionBombError) as e:
            print(f'Inaccessible >> {e} >> {foldername}')
            continue

        # Check if width & height are larger than 500.
        width, height = imageObj.size
        if width > 500 and height > 500:

            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:

            # Image is too small to be a photo.
            numNonPhotoFiles += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > (numPhotoFiles + numNonPhotoFiles) / 2:
        print(os.path.abspath(foldername))
