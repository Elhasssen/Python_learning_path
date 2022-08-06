# your regular clock can schedule prograls to run code at 
# some spedified time ot date at a regular intervals
# Python's time and datetime modules provide these functions

# you can lauch by scheduling with the subprocess 
# and threading modules

# the time module 

# the time.time() and time.sleep() ate the most uselful in the time module 
 
# the time.time() function

# the unix epoch is a time reference commonly used in programming
# which is january 1st, 1970 
# ###########################
# import time 

# print(time.time())
# # output : 1646128421.7190385
# # the retrun value is how many seconds have passed between the unix
# # time and the current time
########################################
# the epoch timestamps can be used to mesure how long 
# a piece of code takes to run 

# import time 
# def calcProd():
#     # Calculate the product of the first 100.000 numbers
#     product = 1
#     for i in range(1,100000):
#         product = product * i
#     return product

# startTime = time.time()
# prod = calcProd()
# endTime = time.time()
# print('The result is %s digits long.'%(len(str(prod))))
# # in order to know how many seconds it took the 
# # program to run is the current time minus the Unix epoch
# print('Took %s seconds to calculate.' % (endTime - startTime))

#################################################
# # tthe return value of time.time() is useful but not human-readable

# import time

# print(time.ctime())
# thisMoment = time.time()
# print(time.ctime(thisMoment))
######################################################
# # the time.sleep() fucntion 
# # if you want your program to pause for a while 
# # all you have to do is to call the time.sleep()
# # and give it how many second the program will be pause 

# import time 
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)

###################################### 
# # rounding numbers
# import time
# now = time.time()
# print(now)
# print(round(now,2))
# print(round(now,4))
# print(round(now))
##############################
# the datetime module 
# import datetime

# print(datetime.datetime.now())
# dt = datetime.datetime(2019,10,21,16,29,0)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
###############
# testing
# halloween2019 = datetime.datetime(2019,10,31,0,0,0)
# newyear2020 = datetime.datetime(2020,1,1,0,0,0)
# oct31_2019 = datetime.datetime(2019,10,31,0,0,0)

# if halloween2019 == oct31_2019 : print("True")
# if halloween2019 < newyear2020 :
#     print('false')
# if newyear2020 > halloween2019 :
#     print('true')
# if newyear2020 != oct31_2019 : print('True')
###################
# # the timedelta data type
# # the timedelta dta type represent a duration rather than a
# # moment in time
# import datetime
# delta = datetime.timedelta(days=11, hours=10 , minutes=9, seconds=8)
# print(delta.total_seconds())
# # Output : 986948.0
# # in order to get the minutes and dates and etcc , i just have to devide on 60 pretty simple hunh 
#####################################""
# # pausing until a specific date 

# import datetime
# import time

# halloween2016 = datetime.datetime(2016,10,31,0,0,0)
# while datetime.datetime.now() < halloween2016:
#     time.sleep(1)

###########################
# multithreding
# lunch some program as a new thread 
