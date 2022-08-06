#! python3
# downloadXkcd.py  - download every single XKCD comic

import requests, os, bs4
import pathlib
from pathlib import Path

# here is what the program does
# loads the XKCD home page
# saves the comic image on that page
# follows the previous comink link
# repeats until it reaches the first comic
os.chdir('/home/elhassen/Desktop')
# we change dir
url = 'https://xkcd.com' # starting URL 

os.makedirs('comics/xkcd', exist_ok=True) # store comics in ./xkcd
# the exist.ok prevent the program from throwing an expetions
# if the folder already exists
while not url.endswith('#'):
    # download the webpage
    print('Downloading page %s' %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    # find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else: 
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' %comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        # save the image to ./xkcd.
        imagefile = open(os.path.join('comics/xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
    # get the previous button's URL
    prevlink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevlink.get('href')
print('done')

