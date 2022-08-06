#! python3
# seachpyip.py - opens several search results

import re
import requests, sys, webbrowser, bs4

print('searching') # display text while downloading search results

res = requests.get( 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
res.raise_for_status()
# retreibe top search result links
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# as we inspect element we realize that the search resukt
# has Class named 'package-snippet' as a common name
###
# no we open web browsers for each result
linkelem = soup.select('.package-snippet')
# linkelem = [<a class="package-snippet" href="/project/automate/">
# <h3 class="package-snippet__title">
# <span class="package-snippet__name...etc
for i in range(5):
    urltoopen = 'https://pypi.org' + linkelem[i].get('href')
    print('opening',urltoopen)
    webbrowser.open(urltoopen)
