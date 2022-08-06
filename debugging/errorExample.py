import traceback
import os 
from pathlib import Path


os.chdir('/home/elhassen/Desktop/Python/learningpy/debugging')

def spam():
    bacon()

def bacon():
    try:
        raise Exception('This is the error message')
    except:
        #the except statement will gracefully handle
        #the error
        errorfile = open('errorInfo.txt','w')
        errorfile.write(traceback.format_exc())
        # we can write the traceback and store it 
        # into a text, so we can avoid the program
        # from crashing
        # the traceback can obtained from the
        # traceback.format_exc()
        errorfile.close()
        print('The traceback info was written to errorinfo.txt')
spam()
