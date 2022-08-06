#! python3
# StopWatch.py - a simple stopwatch program

import time
# Display the program's instructions 
print('Press ENTER to begin, Afterward, press ENTER to "click" the stopwatch, Press Ctrl-C to quit.')
input()     # Press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1
# Start tracking the lap times 
try:
    while True:
        input()
        # so lapTime is equals to current time minus 
        # lastTime so in the case of the first lap
        # the last time is the start time 
        lapTime = round(time.time() - lastTime, 2)
        # the total time is current time minus 
        # the start time 
        totalTime = round(time.time() - startTime)
        print('Lap #%s: %s (%s)' % (lapNum,totalTime,lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exeption to keep its error message
    # from displaying 
    print('\nDone')
        