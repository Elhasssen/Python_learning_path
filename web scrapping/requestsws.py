# the request module lets you easily download files
# from the web without worrying about complicated
# issues such as network errors and connection problems


###############################
# import requests
# # there will be an error when you name the python file 
# # requests.py so beware the naming of files!!!!


# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# # the requests.get() function will return a value you can 
# # see that it returns a response objects
# print(requests.codes.ok)
# print(res.status_code)
# # so we check the if the request has ssucceded by comparing the 
# # the status code of the request with the value of 
# # requests.codes.ok , so the https code for ok is 200 
# print(requests.codes.ok == res.status_code)
# # the value returned True with everything went finerrr
# print(type(res))
#######################"
# checking for errors 
######
# import requests

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')

# res.raise_for_status()
# the raise_fot_status() method is good way to ensure
# the program halts if a bad download occurs
################
# so we can handle this error without crashing

# import requests

# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')

# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('there was a problem: %s' % (exc))
# note : always call res.raise_for_status so we can ensure the the download
# actually worked
##############################
# saving downloaded file to the hard drive
# import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# res.raise_for_status()
# playfile = open('RomeoAndJuliet.txt','wb')
# # we need to write in writebinary to conserve the unicode encoding
# for chunk in res.iter_content(100000):
#     # iter_content(100000) function returns chunks
#     # of the file
#     # each chunk is of bytes data type, this is actually 
#     # the size of the chunck to be read by the memory 
#     # because sometimes files can be bigger
#     playfile.write(chunk)

# playfile.close()


###################
# HTML 
# parsing HTML with bs4 Module
# creating a beautifulsoup object from HTML

# import requests, bs4

# res = requests.get('https://nostarch.com/')
# print(res.raise_for_status())
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# # the requests.get() will return a response to bs4.beautifulsoup()
# print(type(noStarchSoup))

# examplefile = open('learningpy/web scrapping/example.html')
# exampleSoup = bs4.BeautifulSoup(examplefile,'html.parser')
# # the html.parser comes with python

###############
# finding an Element with the select() Method
# you can retreive web page elements from bs4 calling
# the select() method and passing a string of css selector
# selectors work as regular expressions 
# examples of CSS Selectors : 
# soup.select('div') -------> all elements name <div>
# soup.select(#author) -------> the element with an id of author
# soup.select('.notice') -------> all elements that use a css class names notice
# soup.select('div span') -------> all elements name <span> that are within an element names name <div> 
# soup.select('div > span') -------> all elements names span that are directly with an element name <div> with no element in between
# soup.select('input[name]') -------> all elements named <input> that have a name attribute with any value
# soup.select('input[type = "button"]) -------> all elements name <input> that have an attribute named type with value button
# note : a various selector can be combined to match a more complicated matches 

# in order to get the selector of any specific element we use the inspect element function and compy the element selector

# import bs4

# exampleFile = open('learningpy/web scrapping/example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems))
# print(len(elems))
# # output : 1 it tells us that there is one tag in the list
# print(type(elems[0]))
# # output : <class 'bs4.element.Tag'>
# print(str(elems[0]))
# # output : <span id="author">Al Sweigart</span>
# print(elems[0].get_text())
# # output : Al Sweigart give us the text between the tags
# print(elems[0].attrs)
# # output : {'id': 'author'} gives us a dictionnary of the elements attributs

# pelems = exampleSoup.select('p')
# print(str(pelems[0]))
# # output : <p>Download my <strong>Python</strong> book from <a href="https://
# # inventwithpython.com">my website</a>.</p>
# print(pelems[0].get_text())
# # output : Download my Python book from my website.
# print(str(pelems[1]))
# # output :<p class="slogan">Learn Python the easy way!</p>
# print(pelems[1].get_text())
# # output : Learn Python the easy way!
# # the select() gives three matches
# # we store it in pelems
# # using string to show the elements as strings
# # and using gettext() gives us the elemens text 
#################################################
# getting data from an elements's attributs 

import bs4

soup = bs4.BeautifulSoup(open('learningpy/web scrapping/example.html'),'html.parser')
spanelem = soup.select('span')[0]
# this will return the first item of the list in this case there is only one span
print(str(spanelem))

print(spanelem.get('id'))
# this will retreive : author the attribute of 'id'

print(spanelem.get('some_nonexistant_addr') == None)
# this will verify if that addr exist

print(spanelem.attrs) 
# this will return a dictionnary of attributes

