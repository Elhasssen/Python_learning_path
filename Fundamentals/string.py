
# spam = 'Hello, world!'

# print(spam.upper())

# spam.upper() and spam.lower()

# # in case of mixed input with lower and upper lettercases
# Feeling = input('How are you feeling today\n')

# if Feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is')

# while true meaning looping forever till using the break command
###################################################
# while True:
#     age = input('Enter your age : \n')
#     # if the input is all decimal then it breaks
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age')

# while True: 
#     password = input('Select a new password (letter and numbers only)\n')
#     # isalnum() checks if the input has both decimal and letter
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and numbers')
    
# while True:
#     confirmed_password = input('Please confirm your password\n')
#     if confirmed_password == password:
#         break
#     print('Please validate your password')    
#################################################""

#isalpha() Returns True if the string consists only of letters and isn’t blank
#isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank
#istitle() Returns True if the string consists only of words that begin with an uppercase letter followed by
#only lowercase letters



# startwith() or endswith() verifies if the 
# string starts or ends with that value


##################

#.join() is useful when have a list of 
#string that needs to be joined together

# print('|'.join(['cats','rats','bats']))


# and the .split() method does the opposite you can use
# at what criteria it plits the string with! 

print('my name is elhassen'.split())


#######################""

# .partition() method return a tuple of divided text

# print('my name is elhassen'.partition('name'))

################################

# justifying text
# r.just() right justify a text 
# center centers the text 
# strip() take of spaces, lstrip() and rstrip()
# spam.strip('ampS') will tell it to strip occurrences of a , m , p , and capital S from the ends of
# the string stored in spam .
####################################
# def printpicnic(itemDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth,'-'))
#     for k,v in itemDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

# printpicnic(picnicItems,12,5)
# printpicnic(picnicItems, 20, 6)
#######################################


import pyperclip
r=pyperclip.paste()
print(r)






