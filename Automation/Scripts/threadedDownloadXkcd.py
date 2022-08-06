#! python3
# threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find the url of the comci image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('could not find comic page')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()
            # save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()

# create and start the thread objects
downloadThreads = []   # a lisr of all the Thread objects
for i in range(0, 140, 10):  
    # loops 14 times, creates 14 threads
    # range will from 0 to 140 with steps of 10 
    # that means i = 0 then i = 10 then 20 and so on 
    start = i 
    end = i + 9 
    if start == 0:
        start = 1 # the is no comic 0, so set it to 1. 
    downloadthread = threading.Thread(target=downloadXkcd(start, end))
    downloadThreads.append(downloadthread)
    downloadthread.start()


# waiting all the threads to end 
# in order to do that, we have to call the join() function
# to not run any code on the main thread which is the global code
for downloadthread in downloadThreads:
    downloadthread.join()

print('Done.')

