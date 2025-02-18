'''
By changing the lamda function to hold the on_table -1 and y + 1 we are forcing the number of sticks for the opponent to always have them left,
just so the robot takes a number of sticks that minimizes its outcome to lose.
'''
from collections import namedtuple
import random

Bot = namedtuple('Bot', ('name', 'make_move'))

def create_bot(x, y):
    return Bot(
        # Edit next two lines to create your bot
        name = 'Andrew Bot',
        make_move = lambda on_table: (on_table - 1) % (y + 1) or random.randint(1, y)
    )

# Uncomment next line to show all game logs.  Default: show only lost games.
log_all_games = True