import subprocess

#############################################
# subprocess.Popen('C:\Windows\System32\\calc.exe')
# # this will open the calculator application 
# # the P in Popen() stand for process
############################

# paintProc = subprocess.Popen('c:\\Windows\\System32\\mspaint.exe')

# if paintProc.poll() == None : print('True')
# paintProc.wait()
# print(paintProc.poll())
# # output : is 0 , which the exit code 
# # so the poll() function will ask the driver are we there yet
# # and will return None is the process is still running 
# # and if the process has terminated it will  return the exit code 
# # of 0 
# # the wait() function is like waiting until the driver 
# # has arrived to the destination, so it will bloack untill
# # the launch process ahs been terminated 
######################################
# Passing Command line argument to the Popen() Function 
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\\ElHassen\\Desktop\\Python\\RomeoAndJuliet.txt'])
#########################################################
# Task scheduler, launchd, and cron
# there are avaialabel in the operating systems
###########################################
# opening websites with python 
# the webbrowser.open() will launch a webbroser with the required website
##########################################
# # Running other pything script 
# subprocess.Popen(['C:\\Users\\ElHassen\\AppData\\Local\\Programs\\Python\\Python37\\python.exe', 'C:\\Users\\ElHassen\\Desktop\\Python\\learningpy\\automation\\threadedDownloadXkcd.py'])
#########################################

