import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


romans = {'I': 1,'V': 5, 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}

RomNum = input('please enter a Roman number to translate\n').upper()
logging.debug(f' this is the romans to be translated {RomNum}\n')
# Note : 
# M > D > C > L > X > V > I 
# ex: MCMXCIV, MCMIV

integer = 0 
logging.debug(f'the integer is intilized at {integer}\n')
i = 0
logging.debug(f'the iterator i is intilized at {i}\n')
logging.debug('Start of translations\n')
while i < len(RomNum):
    logging.debug(f'the iterator i {i} is smaller than the roman length {len(RomNum)} to be translated as well as we see \n')
    if i + 1 < len(RomNum):
        logging.debug(f' the indicator of the next symbol {i+1} is smaller that the roman length {len(RomNum)} \n')
        if romans[RomNum[i]] >= romans[RomNum[i + 1]]:
            logging.debug(f' if the symbol at postition  {i} is greater than the symbol at the postion {i + 1} we add the symbol at the postiong {i}')
            integer = integer + romans[RomNum[i]] 
            logging.debug(f'the value of the integer is {integer}')
            i = i + 1
            logging.debug(f'the indicator i value is {i}, we slide by one symbol')
        else: 
            logging.debug(f' if the symbol at postition  {i} is lesser than the symbol at the postion {i + 1} we add the subtracted value of postion {i} from postition {i+1} ')
            integer = integer + (romans[RomNum[i + 1]] - romans[RomNum[i]])
            logging.debug(f'the value of the integer is {integer}')
            i = i + 2
            logging.debug(f'the indicator i value is {i}')
    

logging.debug(f'the value of the integer is {integer}')
print(integer)

