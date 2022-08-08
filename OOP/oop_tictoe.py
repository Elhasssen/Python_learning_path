# tictactoe.py - An OOP tic-tac-toe game.

ALL_SPACES = list('123456789')
X, O, BLANK = 'X', 'O', ' ' # Constants for string values

def main():
    """Runs a game of tic-tac-toe"""
    print('Welcome to tic-tac-toe!')
    gameBoard = TTTboard() # Create a TTT board dictionary
    currentPlayer, nextPlayer = X, O # X goes first, 0 goes next.
    while True:
        print(gameBoard.getBoardStr())
        # keep asking the player until they enter a number 1-9:
        move = None
        while not gameBoard.isValidSpace(move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer)
        # check if the game is over:
        if gameBoard.isWinner(currentPlayer):
            print(gameBoard.getBoardStr())
            print(currentPlayer + 'has won the game!')
            break
        elif gameBoard.isBoardFull(): # Next check for a tie
            print(gameBoard.getBoardStr())
            print('The game is a tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer # Swap turns
    print('Thanks for playing')


class TTTboard:
    def __init__(self, usePrettyBoard =False, UseLogging =False):
        """Create a new, blank tic tac toe board."""
        self._spaces = {} # The board is represented as a Python dictionary
        for space in ALL_SPACES:
            self._spaces[space] = BLANK # All Spaces Start as blank
    def getBoardStr(self):
        """Return a text-representation of the board"""
        return f'''
            {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
            -+-+-
            {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
            -+-+-
            {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9
            '''
    def isValidSpace(self,space):
        """Returns True if the space on the board is a valid space
        number and the space is blank"""
        return space in ALL_SPACES and self._spaces[space] == BLANK
    def isWinner(self,player):
        """Return True if player is a winner on the TTTBoard"""
        b, p = self._spaces, player # Shorter names as "syntactic sugar"
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals
        return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or 
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or 
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))
    def isBoardFull(self):
        """Return True if every sace on the board has been taken"""
        for space in ALL_SPACES:
            if self._spaces[space] == BLANK:
                return False # if a single space is blank, return False
        return True # No spaces are blank, so return True
    def updateBoard(self,space,player):
        """Sets the space on the board to player."""
        self._spaces[space] = player



if __name__ == '__main__':
    main() # call main() if this module is run, but not when imported


    