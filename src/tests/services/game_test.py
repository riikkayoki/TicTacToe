import unittest
from services.game import Game
from services.game_board import GameBoard

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game_board = GameBoard()

    def test_check_for_space(self):
        self.assertTrue(self.game.check_for_space(0, 0, self.game_board.board))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.assertFalse(self.game.check_for_space(0, 0, self.game_board.board))

    def test_check_win_vertical(self):
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.game.insert_move('X', 0, 1, self.game_board.board)
        self.game.insert_move('X', 0, 2, self.game_board.board)
        self.game.insert_move('X', 0, 3, self.game_board.board)
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 0, 4, self.game_board.board)
        self.assertTrue(self.game.check_win(self.game_board.board, self.game_board.board_size))

    def test_check_win_vertical_minus(self):
        self.game.insert_move('X', 1, 19, self.game_board.board)
        self.game.insert_move('X', 1, 18, self.game_board.board)
        self.game.insert_move('X', 1, 17, self.game_board.board)
        self.game.insert_move('X', 1, 16, self.game_board.board)
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 1, 15, self.game_board.board)
        self.assertTrue(self.game.check_win(self.game_board.board, self.game_board.board_size))


    def test_check_win_horizontal(self):
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.game.insert_move('X', 1, 0, self.game_board.board)
        self.game.insert_move('X', 2, 0, self.game_board.board)
        self.game.insert_move('X', 3, 0, self.game_board.board)
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 4, 0, self.game_board.board)
        self.assertTrue(self.game.check_win(self.game_board.board, self.game_board.board_size))

    def test_check_win_desc_diagonal(self):
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 0, 0, self.game_board.board)
        self.game.insert_move('X', 1, 1, self.game_board.board)
        self.game.insert_move('X', 2, 2, self.game_board.board)
        self.game.insert_move('X', 3, 3, self.game_board.board)
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 4, 4, self.game_board.board)
        self.assertTrue(self.game.check_win(self.game_board.board, self.game_board.board_size))

    def test_check_win_asc_diagonal(self):
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 5, 0, self.game_board.board)
        self.game.insert_move('X', 4, 1, self.game_board.board)
        self.game.insert_move('X', 3, 2, self.game_board.board)
        self.game.insert_move('X', 2, 3, self.game_board.board)
        self.assertFalse(self.game.check_win(self.game_board.board, self.game_board.board_size))
        self.game.insert_move('X', 1, 4, self.game_board.board)
        self.assertTrue(self.game.check_win(self.game_board.board, self.game_board.board_size))





