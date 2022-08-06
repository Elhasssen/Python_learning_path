# first we create a tictactoe board like this:
#                    top-L | top-M | top-R
#                    mid-L | mid-M | mid-R
#                    bot-L | bot-M | bot-R

theboard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'bot-L':' ','bot-M':' ','bot-R':' ',}

#function to print tictactoe board

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])


turn = 'X'
for i in range(9):
    printboard(theboard)
    move = input('Turn for' + turn + ' move on which space\n')
    if move =='':break
    theboard[move] = turn
    if turn == 'X':
        turn ='O'
    else:
        turn = 'X'
