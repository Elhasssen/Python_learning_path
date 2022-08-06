import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')


opensym = ['(','[','{']
logging.debug(f'the open symbols are : {opensym}')
closesym = [')',']','}']
logging.debug(f'the closing symbols are : {closesym}')
input = '()[]{}'
logging.debug(f'the input string is  : {input}')
stack = []
logging.debug(f'the stack is empty : {stack}')

for x in input:
    logging.debug(f'we check of the symbol: {x}')
    if x in opensym:
        logging.debug(f'if {x} in open symbols {opensym}')
        stack.append(x)
        logging.debug(f'we add {x} to the stack {stack}')
    elif x in closesym:
        logging.debug(f'if {x} in closing symbols {closesym}')
        pos = closesym.index(x)
        if opensym[pos] == stack[len(stack) - 1] and len(stack) > 0:
            logging.debug(f'if the corresponding {opensym[pos]} opening symbols to {x} is in the stack  {stack}')
            logging.debug(f'we pop the symbols {opensym[pos]} from the stack {stack}')
            stack.pop()
            logging.debug(f'the stack {stack} is now empty')
            
        else :
            logging.debug(f'if there is no corresponding {opensym[pos]} opening symbols is in the stack  and the stack {stack} is empty ')
            print('unbalnced')
if len(stack) == 0:
    logging.debug(f'is the stack {stack} is empty after iterating over the input string {input}')
    print('we print that the input string balanced')
