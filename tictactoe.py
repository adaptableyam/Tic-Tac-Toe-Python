# A tic-tac-toe game built with Python and the TKinter module


from board import *
from logic import *




def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == '__main__':
    main()