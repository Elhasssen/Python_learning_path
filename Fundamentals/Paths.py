import os
from os import path
from pathlib import Path

###############################
# Path('spam','bacon', 'eggs')
# # this will return 
# # ouuput : PosixPath('spam/bacon/eggs')
# str(Path('spam', 'bacon', 'eggs'))
# #this will return 'spam/bacon/eggs'
###############################
# from pathlib import Path
# myfiles = ['accounts.txt','details.csv','invite.docx']
# for filename in myfiles:
#     print(Path(r'/home/elhassen/Desktop/paths',filename))
# # /home/elhassen/Desktop/paths/accounts.txt
# # /home/elhassen/Desktop/paths/details.csv
# # /home/elhassen/Desktop/paths/invite.docx
###################################

# from pathlib import Path 
# Path('spam') / 'bacon' / 'eggs'
# # PosixPath('spam/bacon/eggs')
# Path('spam') / Path('bacon/eggs')
# # PosixPath('spam/bacon/eggs')
# Path('spam') / Path('bacon','eggs')
# # PosixPath('spam/bacon/eggs')

#####################################
# from pathlib import Path

# homefolder = r'/home/elhassen/Desktop/paths'
# subfolder = 'spam'
# print(homefolder + '/' + subfolder)
# # output : /home/elhassen/Desktop/paths
# print('/'.join([homefolder, subfolder]))
# # output : /home/elhassen/Desktop/paths

####################################
# # the current working dirrectory
# print(Path.cwd())
# # Output : /home/elhassen/Desktop/Python
# os.chdir('/home/elhassen/Desktop/Python/learningpy')
# print(Path.cwd())
# # changed working directory: /home/elhassen/Desktop/Python/learningpy
#######################################
# # The Home directory
# print(Path.home())
# # output : /home/elhassen
##########################################
# # Creating new Folders Using the os.makedirs() function
# os.makedirs('/home/elhassen/Desktop/Python/learningpy/test')
# # output : this creates a new folder names test 
##########################################
# # Handling absolute and relative Paths
# print(Path.cwd().is_absolute())
# # this will reveal if the path is absolute or not
# # get an absolute path from a relative path
# print(Path.cwd() / Path('Paths.py'))
############################################
# Getting the parts of a File Path
# p = Path('/home/elhassen/Desktop/Python/learningpy/Paths.py')
# print(p.anchor) # output: /
# print(p.name)   # outout: Paths.py
# print(p.stem)   # output: Paths
# print(p.suffix) # output: .py
# print(p.drive)  # output: empty since it is linux
# print(Path.cwd())
# # Output : /home/elhassen/Desktop/Python/learningpy
# print(Path.cwd().parents[0])
# # output : /home/elhassen/Desktop/Python
# print(Path.cwd().parents[1])
# # output : /home/elhassen/Desktop
# # and so on 
# # getting the dir and the base name 
# filepath = '/home/elhassen/Desktop/Python/learningpy/Paths.py'
# print(os.path.basename(filepath)) 
# # output : Paths.py
# print(os.path.dirname(filepath))
# # output : /home/elhassen/Desktop/Python/learningpy
# # getting both together 
# print(os.path.split(filepath))
# # ('/home/elhassen/Desktop/Python/learningpy', 'Paths.py')
# # or 
# print(os.path.basename(filepath),(os.path.dirname(filepath)))
# split path 
# print(filepath.split(os.sep))
# # output : ['', 'home', 'elhassen', 'Desktop', 'Python', 'learningpy', 'Paths.py']
###################################################
# # Finding File Sizes and Folder Contents
# # finding file size
# print(os.path.getsize('/home/elhassen/Desktop/paths/Debt.txt'))
# # Output : 126
# print(os.listdir('/home/elhassen/Desktop/paths'))
# # Output : ['Debt updated.txt', 'Debt.txt']
###################################
# # to find out the total size 
# totalsize = 0
# for filename in os.listdir('/home/elhassen/Desktop/paths'):
#     totalsize = totalsize + os.path.getsize(os.path.join(os.path.join('/home/elhassen/Desktop/paths'), filename))
# print(totalsize)
# # output : 222
#########################################
# # Modifying a list of files using Glob Patterns
# p = Path('/home/elhassen/Desktop/paths')
# print(p.glob('*'))
# # output : <generator object Path.glob at 0x7fbbda750dd0>
# print(list(p.glob('*')))
# # output : [PosixPath('/home/elhassen/Desktop/paths/Debt updated.txt'), PosixPath('/home/elhassen/Desktop/paths/Debt.txt')]
# # the * will get multiple of any charachters
# # like with regexes you can create complex expressions
# print(list(p.glob('*.txt')))
###########################################
# we can use * to make complex expressions
# p = Path('/home/elhassen/Desktop/paths')
# print(list(p.glob('*.?x?')))
#[ out putPosixPath('/home/elhassen/Desktop/paths/Debt updated.txt'), PosixPath('/home/elhassen/Desktop/paths/Debt.txt')]
###########################################
# we can iterate of the generator 
# p = Path('/home/elhassen/Desktop/paths')
# for textFilePathob in p.glob('*.txt'):
#     print(textFilePathob) # Prints the Path object as a string.
# Output : 
# /home/elhassen/Desktop/paths/Debt updated.txt
# /home/elhassen/Desktop/paths/Debt.txt
###########################################
# # Checking Path Validity
# # PS: calling p.exists() returns true if the path exists
# #     calling p.is_file() returns true if the path exists and is a file
# #     calling p.is_dir() returns true if the path exists and is a directory
# homepath = Path('/home')
# notexist = Path('/bla/bla')
# textfile = Path('/home/elhassen/Desktop/paths/Debt.txt')
# print(homepath.exists())
# # output: True
# print(homepath.is_dir())
# # output: True
# print(notexist.exists())
# # output: False
# print(textfile.is_file())
# # output: True
# print(textfile.is_dir())
# # output: False
# ####################################
# File reading\Writing process
# from pathlib import Path 
# p = Path('/home/elhassen/Desktop/paths/Debt.txt')
# p.write_text('Hello, world!')
# # this function writes into the file
# print(p.read_text())
# # this function will read it 
# # input : Hello, world!
########################################
# from pathlib import Path 
# hellofile = open(Path.home() / 'helloword.txt')
# # the open funtion can also accept strings
# # readiing the content of a files : 
# helloContent = hellofile.read()
# print(helloContent)
# # we can also get a list of values from files using readline() function
# poetryfile = open(Path.home() / 'helloword.txt')
# print(poetryfile.readlines())
## outputs:['today i woke up unwhole\n', 'missing soneone who could have been my own\n', 'but life is tragic and unknown\n', 'all we can do is finding the zone \n', '\n']
##################################################
# # writing to files : 
# tomatofile = open('tomato.txt', 'w')
# # w makes the file in writing mode
# tomatofile.write('Hello, world!\n')
# tomatofile.close()
# tomatofile = open('tomato.txt','a')
# # a makes the file in append mode to add some text
# tomatofile.write('Tomato is not a vegetable not a fruit')
# tomatofile.close()
# tomatofile = open('tomato.txt')
# content = tomatofile.read()
# tomatofile.close()
# print(content)
# # write() function will create the tomato file since it is not 
# # there yet,
# # Output : Hello, world!
# # Tomato is not a vegetable neither a fruit.
#################################################
# # saving variables with shelve Module
# import shelve
# # shelve helps you store data, and let the load them the next time they are run
# shelfile = shelve.open('mydata')
# cats = ['Zophie','Pooka','Simon']
# shelfile['cats'] = cats
# shelfile.close()
# # now we open 
# shelfile = shelve.open('mydata')
# print(type(shelfile))
# # output : <class 'shelve.DbfilenameShelf'>
# print(shelfile['cats'])
# # output : ['Zophie', 'Pooka', 'Simon']
# shelfile.close()
# # when we close the shelf you can print its contents
# # shelves modules have keys and values just like dictionnaries
# shelfile = shelve.open('mydata')
# print(list(shelfile.keys()))
# # output : ['cats']
# print(list(shelfile.values()))
# # output : [['Zophie', 'Pooka', 'Simon']]
###################################################
# # Saving variables with the pprint.pformat() function
# import pprint
# cats = [{'name' :'Zophie','desc' :'chubby'},{'name' : 'Pooka', 'desc' : 'fluffy'}]
# pprint.pformat(cats)
# # turn the cats dictionnary to a string so we can write it into a file
# fileobj = open('mycats.py', 'w')
# # the import function are just python scripts
# # When the string from pprint.pformat() is saved to a .py ﬁle,
# # the file is a module to be imported 
# fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileobj.close()
# # since now the cats is a python file
# # since they can be imported
# import mycats
# print(mycats.cats)
# # we print the fitst object of the dictionaaary
# print(mycats.cats[0])
# # we print the name if the of the first object or cat
# print(mycats.cats[0]['name'])
########################################################


