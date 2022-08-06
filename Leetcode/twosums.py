
import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

lengArray = int(input('plaese enter the length of the array!\n'))
array = []
for i in range(lengArray):
    value = int(input(f'please enter the values, value number {i+1}\n'))
    array.append(value)



number = int(input('Please enter a number:\n'))
indexes = []
for i in range(len(array)):
    # the problem was that the j gets intitalized everytime 
    # the solution was to specifiy the range function at what value starts the variable j
    for j in range(i + 1,len(array)):
        logging.debug(f'the value of i is {i}')
        logging.debug(f'the value of j is {j}')
        if array[j] + array[i] == number:
            indexes.append(i)
            indexes.append(j)



print(f'the indexes that sums to {number} of the {array} are {indexes}')

