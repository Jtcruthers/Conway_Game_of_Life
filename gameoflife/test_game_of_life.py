from unittest import TestCase
from unittest.mock import patch
from gameoflife import game_of_life

class TestGameOfLife(TestCase):

    @patch('game_of_life.create_board')
    @patch('game_of_life.run_simulation')
    @patch('game_of_life.print_board')
    def test_collaborator(self, mock_create_board, mock_run_simulation, mock_print_board):
        game_of_life.run()

        assert mock_create_board.called
        assert mock_run_simulation.called
        assert mock_print_board.called