import re

#| pipe will return one of either both expressions
###########
# Pipe will return the first occurent in the string
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
############
#Pipe can also be used to match several patterns 
#using the parentheses
################
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
####################
# Optional matching using the question Mark
################################
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('the adventures of Batman')
print(mo1.group())
# the (wo)? means the pattern wo is optional group
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#####################""
# Matching zero or more with the star
# the * the group that has the * may accure more 

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('the Adventures of Batwowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())
#######################################""
# matching specific repetitions with braces
# the {} follower by group will match the specific argument
# put in the braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
# it will no match Ha not HaHa
print(mo1.group())
#############################
greedy and non-greedy expressions
pythin regex are greedy by default

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

###############################
# the findall returns every match

phnoeNumRegex = re.compile(r'\d-\d\d\d-\d\d\d-\d\d\d')
print(phnoeNumRegex.findall('Cell: 0-555-555-555 word: 0-555-555-999'))
####################
# charachter classes
xmaxRegex = re.compile(r'\d+\s\w+')
# \d+ matches a digit or more
# \s matches a space 
# \w+ matches anyletter or more
print(xmaxRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# makes your own charcters, this will match the vowles 
# in the string whilst consonantRegex = re.compile(r'[^aeiouAEIOU]')
# will match the charcters that is not a vowel 
#########################################################""
# The caret and dollar sign characters
# the ^ indicate the match must startwith Hello
beginwithhello = re.compile(r'^Hello')
print(beginwithhello.search('Hello, world!'))
# the dollar sign characters must end with digit as follows
endswithnumber = re.compile(r'\d$')
print(endswithnumber.search('Your Number is 42'))
# you can use both to  match ending and starting with one 
# digit as: re.compile(r'^\d+$')
##############################################"
# the wildcard Character
# the . will match every word that has at and of length 3
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# ouput : ['cat', 'hat', 'sat', 'lat', 'mat']
##############################################
Matching everythign with the dot star that 
comes after a specific word blablabala (.*)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: ElHassen Last Name: sweigart')
print(mo.group(1))
print(mo.group(2))
# the dot star is greedy 
# to limit it
# Non-Greedy
nongreedyregex = re.compile(r'<.*?>')
mo3 = nongreedyregex.findall('<To serve man> for dinner.>')
print(mo3)
# Greedy
greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.findall('<To serve man> for dinner.>')
print(mo4)
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
Output : 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
###############################################
# Case insensetive matching : 
# re.I makes the regex case-insensetive can match
# different ; Robocop, RobotCop
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoBoCop is part man, part machine, all cop.').group())
######################################
substituing string with the sub() Method

namesregex = re.compile(r'(Agent) \w+')
print(namesregex.sub('CENSORED', 'Agent hassen gave some classified secrets'))
censoring names

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent clice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#####################################################""

