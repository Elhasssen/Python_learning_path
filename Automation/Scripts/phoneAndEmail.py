#! python3
# phoneAndEmail.py - finds phone numbers and email adresses on the keyboard 


from typing import Text
import pyperclip, re

phoneRegex = re.compile(r''' (
    (\d(\s|-|\.)?\d{3}|\(\d{4}\))    # 0-555 or (0555)    
    (\s|-|\.)       # - or ' ' or dot
    (\d{3})         # 333 
    (\s|-|\.)       # - or ' ' or dot
    (\d{3})         # 333 

)''',re.VERBOSE)
#re.VERBOSE ignores all the comments within the Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # Username
    @                  # @ symbol
    [a-zA-Z0-9.-]+     # domain name
    (\.[a-zA-Z]{2,4})  # dot-something

)''', re.VERBOSE)

# Find matches in clipboard text
# text = '0444-444-444 and 0777-888-777 and email is hasseneanf16@gmail.com and boumeddiene.elhassen@gmail.com'
text = str(pyperclip.paste())
# 'my number is 0444-444-444 and 0777-888-777 and email is hasseneanf16@gmail.com and boumeddiene.elhassen@gmail.com'
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ''.join(groups[0])
    matches.append(groups[0])
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard 
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard :')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses.')