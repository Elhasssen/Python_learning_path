#! python3
# resizeAndAddLogo.py  - Resizes all images in current working directory to
# fit in 300x300 square, and adds logo.png to the lower-right corner

import os
from PIL import Image
os.chdir('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images')
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open(LOGO_FILENAME).convert('RGBA')
logoIm = logoIm.resize((50, 50))
logoWidth, logoHeight = logoIm.size
os.makedirs('withlogo', exist_ok=True)


# Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME :
        continue # skip non-image files and the logo file itself
    im = Image.open(filename).convert("RGBA")
    width, height = im.size
    # check if the image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE
    # Resize the image
    print('Resizing %s ...' % (filename))
    im = im.resize((width, height))
    print('Adding logo to %s ...' % (filename))
    im.paste(logoIm, ( width - logoWidth, height - logoHeight), logoIm)
    if im.mode != 'RGB':
        im = im.convert('RGB')
    im.thumbnail(im.size, Image.ANTIALIAS)
    im.save(os.path.join('withLogo', filename) , 'JPEG')

# Errors that were fixed : 
#  you need to convert both the logo and the image to the RGBA mode
#  when you try to save the image you have to convert it to RGB
# becaise it won't be saved as RGBA mode
