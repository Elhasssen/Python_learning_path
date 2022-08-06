# we preform input valisation by repeatedly asking
# the user for input

##########################################
# while True:
#     age = input('Please Enter your Age :')
#     try:
#         age = int(age)
        
#     except:
#         print('Please use a numeric digits')
#         continue
#     if age < 1: 
#         print('Please enter a positive number')
#         continue
#     break

# print(f'Your Age is {age}')
##########################################u
# import pyinputplus 
# Pyinputplus has several functions: 
# inputstr()
# inputnum() : ensures the user has put a number
# inputchoice() : ensures the user has put multiple choices
# inputmenu() : is similiar to inputchoice() but provides
# numbered and lettered options
# inputdatetime() : ensures the user enters a date and time
# inputYesNo() : ensures the user enters a yes or no response
# inputbool() : as as before but takes True or False
# inputEmail() ; ensures an email
# inputFilepath() : ensure a valid file path and filename
# inputPassword() : diplays Stars instead of showing sensetive information
####################
# import pyinputplus as pyip
# # this will prompt the user for as long as they enter invalid input
# response = pyip.inputNum()
#################################
from typing import DefaultDict
import pyinputplus as pyip

#################################
# response = pyip.inputInt(prompt= 'Enter a Number\n')
#################################
# min,max,greater than, and less than
#Min
# response = pyip.inputNum('Enter num:', min = 4)
#Greater than 
# response = pyip.inputNum('Enter num :', greaterThan = 4)
#Less than 
# response = pyip.inputNum('>',min = 4, lessThan= 6)
######################
# # The blank keyword argument
# # response = pyip.inputNum('Enter num: ')
# response = pyip.inputNum(blank=True)
# # output = ''
############################
# the limit, timeout, and default keyword arguments
# limit 2 attemps 
# response = pyip.inputNum(limit=2)
#Time out limited time
# response = pyip.inputNum(timeout=4)
# Default keyword argument
# response = pyip.inputNum(limit=2, default='N/A')
########################
# blockregex used to block regexes
# response = pyip.inputNum(blockRegexes = [r'[02468]$'])
# AllowRegexes
#####################""
# Allow regexes
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
# response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
###############################
# Passing a custom Validation Function to inputCustom()

def addsUpToTen(numbers):
    numbersList = numbers.split(' ')
    # or numbersList = list(numbers)
    # it depends on the input string
    # how the user choose to enter his string 
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s' %(sum(numbersList)))
    print("Congrats") 
response = pyip.inputCustom(addsUpToTen) # No parentheses after addsUpToTen here.

