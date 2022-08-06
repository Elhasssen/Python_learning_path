import logging
logging.basicConfig(level= logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
import random
guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('the guess is %s' %guess)
coin = {'0': 'tails', '1': 'heads'}
# 0 is tails, 1 is heads
# the problem was that the random into generates
# integers rathers than string, so we had to match them 
# with the added dictionnary
toss = coin[str(random.randint(0,1))]
logging.debug('the toss is %s' %toss)
if toss == guess:
    print('you got it!')
else:
    print('nope! guess again!')
    guesss = input()
    if toss == guesss:
        print('You got it!')
    else:
        print('Nope, you are really bad at this game!')