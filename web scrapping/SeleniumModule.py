# selennium allows the browser to 
# access the website as of human
# is using the browser 

# some websites use javescript that 
# update the website so we use 
# selenium instead

# a selenium controlled browser
# will download image, advertisment, cookies, and privacy
# invading trackers 

# selenium can be detected by websites and major
# ticketing and ecommerce websites often block 
# browser controlled by selenium to prevent 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://inventwithpython.com')

# to finish later



