# import numpy as np
# from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
# from mctspy.tree.search import MonteCarloTreeSearch
# from mctspy.games.examples.tictactoe import TicTacToeGameState

# state = np.zeros((3,3))
# initial_board_state = TicTacToeGameState(state = state, next_to_move=1)

# root = TwoPlayersGameMonteCarloTreeSearchNode(state = initial_board_state)
# mcts = MonteCarloTreeSearch(root)
# best_node = mcts.best_action(10000)

import numpy as np
from mctspy.tree.nodes import TwoPlayersGameMonteCarloTreeSearchNode
from mctspy.tree.search import MonteCarloTreeSearch
from mctspy.games.examples.connect4 import Connect4GameState

# define inital state
state = np.zeros((7, 7))
starting_player = np.random.choice([-1, 1])
board_state = Connect4GameState(
    state=state, next_to_move=starting_player, win=4)

# link pieces to icons
pieces = {0: " ", 1: "X", -1: "O"}

# print a single row of the board
def stringify(row):
    return " " + " | ".join(map(lambda x: pieces[int(x)], row)) + " "

# display the whole board

def display(board, current_player):
    board = board.copy().T[::-1]
    # print("Current Player: " + pieces[current_player])
    print("============================")
    for row in board[:-1]:
        print(stringify(row))
        print("-"*(len(row)*4-1))
    print(stringify(board[-1]))
    print()

# hiển thị ban đầu
display(board_state.board, board_state.next_to_move)

# keep playing until game terminates
while board_state.game_result is None:
    # calculate best move
    root = TwoPlayersGameMonteCarloTreeSearchNode(state=board_state)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(total_simulation_seconds=1)

    # update board
    board_state = best_node.state
    # display board with current player
    display(board_state.board, board_state.next_to_move)

# print result
# print('==> Result: '+pieces[board_state.game_result]+' win')

if pieces[board_state.game_result] in ['O', 'X']:
    print('==> Result: '+pieces[board_state.game_result]+' win')
else :
    print('==> Result: Draw')