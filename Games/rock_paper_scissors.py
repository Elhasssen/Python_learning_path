import random


def game():
    user = input("'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r','p','s'])


    if user == computer:
        return 'You tied!'

# r>s, s>p, p>r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'




def is_win(player, player2):
    if (player == 'r' and player2 == 's') or (player == 's' and player2 == 'p') or (player == 'p' and player2 == 'r'):
        return True


print(game())