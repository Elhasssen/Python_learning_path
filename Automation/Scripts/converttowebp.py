import os 
from pathlib import Path
from webptools import dwebp
from webptools import grant_permission

grant_permission()
os.chdir('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\automation\\images')
# p = Path.cwd()

source = Path('C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\automation\\images')

for filename in os.listdir(source):
    print(filename)
    if filename.endswith(f'.webp'):
        print('Yes')
        outname = filename[:-4] + "png"
        print(outname)
        dwebp(input_image=filename, output_image=outname, option="-o", logging="-v")

    