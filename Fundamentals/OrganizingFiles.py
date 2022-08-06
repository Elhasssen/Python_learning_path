import os 
from os import path
from pathlib import Path
import shutil
########################
# # change working directory
# os.chdir('/home/elhassen/Desktop/Organize')
# # check if the working directory has changed
# print(Path.cwd())
############################
# copying files and folders
# p = Path.cwd()
####
# shutil.copy() copy the helloword.txt to 
# the destination folder with conserving the name
# helloword.txt
# shutil.copy(p / 'source' / 'helloword.txt', p / 'destination')
####
# the second shutil copy the helloword txt to 
# destination while conserving the name helloword2.txt
# shutil.copy(p / 'source' / 'helloword.txt', p / 'destination/helloword2.txt')
####
# shutil.copytree() will copy and entire folfer and every
# folder and file contained to it
# shutil.copytree(p / 'source', p / 'sourcebackup')
########################
# Moving and Renaming files 
####
# if the file already exists then there will be 
# an error, if not: it will be moves
# shutil.move(p / 'source/helloword.txt', p / 'destination')
####
# # or we can move by specifying the new file name
# shutil.move(p / 'source/helloword.txt', p / 'destination/helloword3.txt')
####
# # the shutil.move() can't find the destination file so it will create a file
# # named as below 
# shutil.move(p / 'source/helloword.txt', p / 'this folder was made by shutil')
####
##################
# deleting files and folders
##################
# dltpath = Path('/home/elhassen/Desktop/Organize/Deleting')
# # os.unlink(path) will delete the file 
# # os.rmdir(path) will delete the folder at path
# # the folder must be empty
# # shutil.rmtree(path) will remove the folder and 
# # whatever it contains 
# for filename in dltpath.glob('*.txt'):
#     os.unlink(filename)
# os.rmtree() can be dangerous to use 
##############
# # delete with send2trash module
# os.chdir('/home/elhassen/Desktop/Organize/Deleting')
# import send2trash
# tomatofile = open('tomato.txt','a') # creates the file
# tomatofile.write('tomato is both veggy and a fruit')

# tomatofile.close()
# send2trash.send2trash('tomato.txt')
##################
# walking a directory tree
# import os 

# for foldername, subfolders, filenames in os.walk('/home/elhassen/Desktop/Organize/Deleting'):
#     print('The current folder is' + foldername)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF' + foldername + ':' + subfolder)
#     for filename in filenames:
#         print('FILE INSIDE ' + foldername + ':' +  filename)
#     print('')

# # the os.walk() return a list of the folder, its subfolders, and its files.
###################
# Reading the ZIP Files 
# import os, zipfile

# os.chdir('/home/elhassen/Desktop/Organize/zipping')
# zipping = Path.cwd()
# # zipfile.ZipFile() reads a zip file
# examplezip = zipfile.ZipFile(zipping / 'example.zip')
# # returns the files containted in the zip file
# print(examplezip.namelist())
# # getinfo() returns about that particular file 
# hwinfo = examplezip.getinfo('helloword3.txt')
# # .file_size will return the size of that file
# print(hwinfo.file_size)
# # .compress_size will compress the file
# print(hwinfo.compress_size)
# # round() has two : the number , and the postion of the digit of the number
# print(f'Compressed file if {round(hwinfo.file_size / hwinfo.compress_size, 2)}x smaller!')
#############
# Extracting from a ZIP file 
# import zipfile
# os.chdir('/home/elhassen/Desktop/Organize/zipping')
# extract = Path.cwd()
# zipfolder = zipfile.ZipFile(extract / 'example.zip')
# # you can specify the directory of the extracted file
# # .extract('helloword.txt') can extract a single file
# # and you can specify the directory 
# # ex :  extract('helloword.txt', 'desired path')
# zipfolder.extractall()
# zipfolder.close()
############################
# Creating and adding to zip files
# import zipfile

# os.chdir('/home/elhassen/Desktop/Organize/zipping')
# p = Path.cwd()
# newzip = zipfile.ZipFile('newzip','w')
# # zip_deflated, this value works well on all sorts of 
# # data
# newzip.write(p / 'helloword3.txt', compress_type=zipfile.ZIP_DEFLATED)
# newzip.close()

###############
#### over and out #####
