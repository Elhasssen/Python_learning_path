import re
# Regular expressions, called regexes for short, 
# are descriptions for a pattern of text.
###################################
# phoneNumRegex = re.compile(r'\d-\d\d\d-\d\d\d-\d\d\d')

# text= 'my phojne number is 0-777-888-999'

# mo = phoneNumRegex.search(text)
# print('phone number found : ' + mo.group())

###############################

# grouping with patantheses 

phoneNumRagex = re.compile(r'(\d)-(\d\d\d)-(\d\d\d)-(\d\d\d)')

mo = phoneNumRagex.search('My number is 0-777-777-777')
blabla = list(mo.groups())

print('-'.join(blabla))