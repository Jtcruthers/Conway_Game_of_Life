from gameoflife.Board import Board
import copy

def run():
    board = create_board(10, 10)
    run_simulation(board)
    print_board(board)


def create_board(height, width):
    """
        Creates the board and seeds it
    """

    board = Board(height, width)
    board.seed()
    return board


def run_simulation(board):
    """
        Runs the entire simulation on a given board
    """

    old_board = copy.deepcopy(board)


def print_board(board):
    """
        Prints the given board
    """

    board.print()
