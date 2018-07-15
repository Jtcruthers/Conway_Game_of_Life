import gameoflife
from curses import wrapper

if __name__ == "__main__":
    wrapper(gameoflife.run)
