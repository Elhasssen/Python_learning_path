# in order to manipluate images you have to understand how 
# computer deals with images 

from PIL import ImageColor

############################################
# print(ImageColor.getcolor('red', 'RGBA'))
# # Output : (255, 0, 0, 255) 
# print(ImageColor.getcolor('black', 'RGBA'))
# # Output : (0, 0, 0, 255)
# print(ImageColor.getcolor('chocolate', 'RGBA'))
# # Output : (210, 105, 30, 255)
# print(ImageColor.getcolor('CornflowerBlue', 'RGBA'))
# # Output : (100, 149, 237, 255)
###########################################
# Cooridnate and box Tuples
# image pixels are addrrssed with X and Y coordinates: 
#####################################
# Manipulating Images with Pillow
#################################
from PIL import Image
import os
os.chdir('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images')
print(os.getcwd())
############################
# catIm = Image.open('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images\\zophie.jpg')
# print(catIm.size)
# # output :(319, 426)
# width, height = catIm.size
# print(width) # Output : 319
# print(height) # Output : 426
# print(catIm.filename) # ouput : C:\Users\ElHassen\Desktop\Python\learningpy\Maniplating images\zophie.jpg
# print(catIm.format)  # ouput : JPEG
# print(catIm.format_description) # output : JPEG (ISO 10918)
##########################################
# Cropping images
# (left,top,right,bottom)
# catIm = Image.open('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images\\zophie.jpg')
# print(catIm.size)
# croppedIm = catIm.crop((200, 190, 270, 280))
# croppedIm.save('cropped.jpg')
###################################
# Copying and pasting image onto other images
# catIm = Image.open('zophie.jpg')
# catCopyIm = catIm.copy()

# faceIm = catIm.crop((200, 190, 270, 280))
# print(faceIm.size)
# catCopyIm.paste(faceIm, (0,0))
# catCopyIm.paste(faceIm, (200, 200))
# catCopyIm.save('pasted.jpg')
#######################################
# Resizing an Image
# from PIL import Image
# catIm = Image.open('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images\\zophie.jpg')
# Width, height = catIm.size
# quartersizedIm = catIm.resize((int(Width / 4), int(height / 4)))
# quartersizedIm.save('quartersized.jpg')

# svelteIm = catIm.resize((Width, height + 100))
# svelteIm.save('svelte.jpg')
###########################################
# rotatting and flipping images

# catIm = Image.open('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\Maniplating images\\zophie.jpg')
# catIm.rotate(90).save('rotated90.jpg')
# catIm.rotate(180).save('rotated180.jpg')
# catIm.rotate(270).save('rotated270.jpg')

##################################################

