import os 
from os import path
from pathlib import Path
import shutil

os.chdir('/home/elhassen/Desktop/Filtering_projects')
p = Path.cwd()

source = Path('/home/elhassen/Desktop/Filtering_projects')
extensions = ['txt','pdf','jpg','png','jpeg','zip','rar','psd','ai']
for files in os.listdir(source):
    for ext in extensions:
        if files.endswith(f'.{ext}'):
            if Path(os.path.join(source,f'{ext}')).is_dir():
                shutil.move(source / files, source / f'{ext}')
            else:
                os.makedirs(source / f'{ext}')
                shutil.move(source / files, source / f'{ext}')
# there is an error when the folder contains a name that is similiar to one of the extentions -----> to fix 


# for files in os.listdir(source):
#     if files.endswith('.txt'):
#         if Path(os.path.join(source,'txt')).is_dir():
#             shutil.move(source / files, source / 'txt')
#         else: 
#             os.makedirs(source / 'txt')
#             shutil.move(source / files, source / 'txt')
#     elif files.endswith('.pdf'):
#         if Path(os.path.join(source,'pdf')).is_dir():
#             shutil.move(source / files, source / 'pdf')
#         else: 
#             os.makedirs(source / 'pdf')
#             shutil.move(source / files, source / 'pdf')
#     elif files.endswith('.jpg'):
#         if Path(os.path.join(source,'jpg')).is_dir():
#             shutil.move(source / files, source / 'jpg')
#         else: 
#             os.makedirs(source / 'jpg')
#             shutil.move(source / files, source / 'jpg')



        
