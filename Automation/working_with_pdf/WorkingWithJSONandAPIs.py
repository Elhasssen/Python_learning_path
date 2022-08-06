# JSON - Javascript object Notation is a popular
# way to format data as a single
# human-readable string. JSON is the native way of 
# Javascript write their data structure 
# so here is an example : 

# {"name":"Zophie","isCat" : true, 
# "miceCaught" : 0, "napsTaken" : 37.5,
#  "felineIQ" : null}

# JSON is a way for programs to interact with websites
# accessing an API is the same as accessing any other webpage
# the data returned by an API is formatted with JSON 
# API aren't easy for people to read 

# Many websites make their data available in JSON format
# Facebook, Twitter, Yahoo, Google, Tumblr; Wikipedia, Flickr 
# IMDb, Rotten tomatoes, LinkedIn,

# Using API you can do things : 
# - Scrape raw data from websites (accessing APIs is often more 
# convenitent than downloading web pages and parsin HTML 
# with beautiful Soup)

# - Automatically download new posts from one of your social 
# network and post them into another 
# example : posting from Tumblr to Facebook
#  
# - Create a "Movie Encyclopedia" for your persoanl movie collection
# by pulling data from IMDb, rotten tomatoes, and wikipedia and putting 
# it into a single text file on your computer

# JSON is not the onyl way to format data into a human-readable-string
# there XML, YML, INI, ASN.1

##########################################
# the JSON Module : 
# the Python JSON Module handles all the details of translating
# between a string with JSON data and python values for the 
# json.loads() and json.Dumps(): 
# PS: JSON can't store every kind of python value;
# it can store only : Strings, integers, floats, booleans,
# lists, dictionnaries, and NoneType, JSON can not 
# represent python-specfic objects ; such as file and 
# csv reader or writer objects , regex objects , or selenium webelement objects
##########################################
# Reading JSON with loads() Function : 
stringOfJsonData = '{"name" : "Zophie", "isCat":true,"miceCaught": 0,"felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
# output
# {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None} 
# Note that JSON strings always use double quotes, it will return
# the data as a python dictionary
##########################################
# Writing JSON with dumps() function
pythonvalue = {'isCat': True, 'miceCaught': 0, 'name':'Zophie', 'felineIQ' : None}
import json
stringOfJsonData = json.dumps(pythonvalue)
print(stringOfJsonData)
# output : 
# {"isCat": true, "miceCaught": 0, "name": "Zophie", "felineIQ": null}

