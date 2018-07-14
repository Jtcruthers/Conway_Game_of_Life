import math, random

class Board():

    def __init__(self, height=10, width=10):
        self.height = height
        self.width = width
        self.board = [[" "for x in range(width)] for x in range(height)]


    def seed(self):
        total_cells = self.height * self.width
        number_of_seeds = math.floor(total_cells * 0.1)
        for _ in range(number_of_seeds):
            seed_index = (random.randint(0,self.height - 1), random.randint(0,self.width - 1))
            self.board[seed_index[0]][seed_index[1]] = "X"


    def print(self):
        for _ in range(50):
            print("-", end="")
        print()
        for row in self.board:
            print(row)
        for _ in range(50):
            print("-", end="")
        print()