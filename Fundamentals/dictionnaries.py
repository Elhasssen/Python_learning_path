from typing import List


birthdays = {'Hassen': 'Fbr 17','Ismat' : 'Dcr 3', 'Ghazali': 'Fbr 2'}
# Display a value in a dictionnary or add non-existant! 

#####################################
# while True: 
    
#     name = input('enter a name : (blank to quit)\n')
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + 'is the birthday of ' + name)
#     else: 
#         print('i do not have birthday information for ' + name)
#         print('what is their birthday')
#         bday = input()
#         birthdays[name] = bday
#         print('Updated!')

#######################################

# Print values in dictionnary 

# for x in birthdays.values():
#     print(x)
####################################
# print keys in dictionnary

# for x in birthdays.keys():
#     print(x)
##########################################
# print items (keys + values) in dictionnary 

# for x in birthdays.items():
#     print(x)

#################################
# passes a dictionnary keys to a list 
# list=list(birthdays.keys())
# print(list)
####################################""

# display the key and value at once 
# for k,v in birthdays.items():
#     print('key' +  k , 'value'+v)

############################

# check if a key exist in a dictionnary
# if 'Hassan' in birthdays.keys():
#     print('True')
# else: print('False')
# PS : you can check the value aswell. 
############################
#or
# if 'Hassen' in birthdays:
#     print('True')
##############################

shop_list = {'milk' : 4, 'lemon' : 3}
# the get() method takes two argument
#the key and a fallback value if the key doesn't exist

# print('i am bringing ' + str(shop_list.get('lemon', 0)) + 'lemon')
# # if the key doesn't exist
# # it will print 0, fallback value
# print('i am bringing ' + str(shop_list.get('cookies', 0)) + 'cookies')
# without using get() the code will throw an error
###################################
# the set_default to check for a key ,
# if the key does exist,it wil return the key value! 
# shop_list.setdefault('almond','10')
# print(shop_list)
# shop_list.setdefault('almond','3')
# print(shop_list)
###########################################



