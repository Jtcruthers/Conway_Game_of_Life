from gameoflife.Board import Board
import time

NUM_OF_SIMS = 10

def run(stdscr):
    board = create_board(stdscr, 10, 10)
    print_board(board)
    for _ in range(1, NUM_OF_SIMS):
        board = run_simulation(board)
        time.sleep(.5)
        print_board(board)


def create_board(stdscr, height, width):
    """
        Creates the board and seeds it
    """

    board = Board(stdscr, height, width)
    board.seed()
    return board


def run_simulation(board):
    """
        Runs the entire simulation on a given board
    """

    new_board = board.copy() 
    for row in range(board.height):
        for column in range(board.width):
            number_of_neighbors_alive = board.get_surrounding_live_cell_count(row, column)

            if number_of_neighbors_alive < 2 or number_of_neighbors_alive > 3:
                new_board.kill_cell(row, column)
            else:
                if not board.is_cell_alive(row, column) and number_of_neighbors_alive == 3:
                    new_board.awaken_cell(row, column)
    return new_board


def print_board(board):
    """
        Prints the given board
    """

    board.print()
