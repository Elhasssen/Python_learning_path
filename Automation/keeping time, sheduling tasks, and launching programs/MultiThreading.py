##################
# Multithreading 

# import threading, time

# # Multithreading is when you launch programs in multi-tasks
 
################
import threading, time

print('Start the program.')
def takeANap():
    time.sleep(5)
    print('Wake up!')
threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of the program.')
# output : 
# Start the program.
# End of the program.
# Wake up
# Notice that the wake up which is the output of the function
# will be displayed in the end. 
# because the takeanap() function has time.sleep(5) so the python program
# will close until it termiante all the threads
#######################
# Passign Agruments to the thread's target Function
# let's say that you want to give the thread arguments and 
# wanted to print these 
# print('Cats','Dogs','Frogs',sep=' & ')

# import threading
# # Kwargs is a keyword argument as sep = ' & ', and args as the lsit that contain cats, dogs and frogs
# threadObj = threading.Thread(target=print, args=['Cats','Dogs','Frogs'], kwargs={'sep' :' & '})
# threadObj.start()

########################""
