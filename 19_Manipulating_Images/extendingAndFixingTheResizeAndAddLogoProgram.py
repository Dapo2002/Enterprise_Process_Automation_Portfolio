# Processes images (.jpg, .png, .gif, .bmp) in a case-insensitive manner,
# pasting a logo in the bottom-right ONLY if the image is at least twice the logo's size.

from PIL import Image
import os

folder = r'C:\Users\Abdulbadie\OneDrive\User\PycharmProjects\My_Python_for_Automation_Journey' \
         r'\19_Manipulating_Images'
os.makedirs(os.path.join(folder, 'withLogo2'), exist_ok=True)
logoFolder = os.path.join(folder, 'withLogo2')

logo = 'catlogo.png'
logoObj = Image.open(logo)
logoWidth, logoHeight = logoObj.size
for image in os.listdir('.'):
    extensions = ('.jpg', '.png', '.gif', '.bmp')
    if not image.lower().endswith(extensions) or image == logo:
        continue
    imageObj = Image.open(image)
    imageWidth, imageHeight = imageObj.size
    if imageWidth < logoWidth * 2 or imageHeight < logoHeight * 2:
        continue
    imageObj.paste(logoObj, (imageWidth - logoWidth, imageHeight - logoHeight), logoObj)
    filename = os.path.splitext(image)[0]
    imageObj.save(os.path.join(logoFolder, f'{filename}_LOGOed.png'))
