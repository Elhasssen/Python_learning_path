#! python3
# bulletPointAdder.py - adds Wikipedia buller points
# to the start of each line of text on the clipboard
import pyperclip

text = pyperclip.paste()

# seperate lines and add lines

lines = text.split('\n')
for i in range(len(lines)): # loop throug all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
print(text)