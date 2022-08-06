#! python3
# mapIt.py - launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line.
    address = ' '.join(sys.argv[1:])
    # the join(sys.argv[1:] will chop the name 
    # the script 
# else: 
#     # get address from clipboard
#     address = pyperclip.paste()
print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)