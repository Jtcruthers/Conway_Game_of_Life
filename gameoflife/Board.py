import math, random, copy

class Board():

    ALIVE = "X"
    DEAD = " "

    def __init__(self, stdscr, height=10, width=10):
        self.stdscr = stdscr
        self.height = height
        self.width = width
        self.board = [[self.DEAD for x in range(width)] for x in range(height)]


    def seed(self, ratio=0.15):
        """
            Seeds the board with random live cells. Can give ratio of live to total cells
        """

        total_cells = self.height * self.width
        number_of_seeds = math.floor(total_cells * ratio)
        for x in range(number_of_seeds):
            seed_index = (random.randint(0,self.height - 1), random.randint(0,self.width - 1))
            self.board[seed_index[0]][seed_index[1]] = self.ALIVE


    def print(self):
        self.stdscr.clear()

        for _ in range(50):
            self.stdscr.addstr("-")
        self.stdscr.addstr("\n")
        for row in self.board:
            self.stdscr.addstr(f"{row}\n")
        for _ in range(50):
            self.stdscr.addstr("-")
        self.stdscr.addstr("\n")
        self.stdscr.refresh()



    def get_surrounding_live_cell_count(self, row, column):
        count = 0
        count += 1 if self.is_cell_alive(row - 1, column - 1) else 0
        count += 1 if self.is_cell_alive(row - 1, column) else 0
        count += 1 if self.is_cell_alive(row - 1, column + 1) else 0
        count += 1 if self.is_cell_alive(row, column - 1) else 0
        count += 1 if self.is_cell_alive(row, column + 1) else 0
        count += 1 if self.is_cell_alive(row + 1, column - 1) else 0
        count += 1 if self.is_cell_alive(row + 1, column) else 0
        count += 1 if self.is_cell_alive(row + 1, column + 1) else 0
        return count


    def is_cell_alive(self, row, column):
        try:
            return self.board[row][column] == self.ALIVE
        except IndexError:
            return False


    def kill_cell(self, row, column):
        self.board[row][column] = self.DEAD


    def awaken_cell(self, row, column):
        self.board[row][column] = self.ALIVE


    def copy(self):
        new_board = Board(self.stdscr, self.height, self.width)
        new_board.board = copy.deepcopy(self.board)
        return new_board 
