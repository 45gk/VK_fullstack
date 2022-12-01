import unittest
import main
from unittest.mock import patch

game1 = main.TicTacGame()


class TestStringMethods(unittest.TestCase):

    def test_val1(self):
        game1 = main.TicTacGame()
        self.assertEqual(game1.validate_input(3), 3)

    def test_val2(self):
        game2 = main.TicTacGame()
        self.assertEqual(game2.validate_input(4), 4)

    def test_val3(self):
        game3 = main.TicTacGame()
        self.assertEqual(game3.validate_input(6), 6)

    def test_val4(self):
        game4 = main.TicTacGame()
        self.assertEqual(game4.validate_input(5), 5)

    def test_makepoint1(self):
        game5 = main.TicTacGame()
        board_check1 = game5.board
        what = "X"
        board_check1[4] = what
        self.assertEqual(game5.make_point(4, "X"), board_check1)

    def test_makepoint2(self):
        game6 = main.TicTacGame()
        board_check2 = game6.board
        what = "O"
        board_check2[5] = what
        self.assertEqual(game6.make_point(5, "O"), board_check2)

    def test_makepoint3(self):
        game7 = main.TicTacGame()
        board_check3 = game7.board
        what = "X"
        board_check3[8] = what
        self.assertEqual(game7.make_point(8, "X"), board_check3)


if __name__ == '__main__':
    unittest.main()
