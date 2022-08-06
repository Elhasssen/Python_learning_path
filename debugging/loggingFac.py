import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(1,n+1) : 
        total *= i
        logging.debug('i is' + str(i) + ',total is' + str(total))
    logging.debug('end of factotial(%s)' %(n))
    return(total)
    # the logging.debug() will print the message
print(factorial(5))
logging.debug('End of program')

# don't use the name of logging.py as your python script
# it might prevent the script from running and you
# face an error

# logging can help us undersatnd what is happening in our code
# and in what order

# you can simply disable log messages by 
# logging.disable(logging.CRITICAL)

# Logging levels

# logging.debug() - used for small details
# logging.info()  - used for general details about working points in the program
# logging.warning() - used to indicate a potential problem that might do something in the future but will keep the program working
# logging.error() - used to record an error that made the program to do something


# logging to a file 
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')