import numpy as np
from colorama import init, Fore

init(autoreset=True)


class TicTacGame:
    """Блок-конструктор"""
    def __init__(self):

        self.inputs = []
        self.BOARD_SIZE = 3
        self.board = {nums: nums for nums in range(1, self.BOARD_SIZE ** 2 + 1)}
        self.WIN_TACTICS = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                            (2, 5, 8), (3, 5, 9), (1, 5, 9), (3, 5, 7))

    """Функция, отображающая доску"""
    def show_board(self):

        print("----------")
        count = 1

        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.board[count] == "X":
                    print(Fore.BLUE + self.board[count], end="|")
                elif self.board[count] == "O":
                    print(Fore.RED + self.board[count], end="|")
                else:
                    print(self.board[count], end="|")
                count += 1
            print()

        print("----------")

    """Функция, принимающая точку, куда пользователь поставит крестик или нолик"""
    def validate_input(self, input_1):
        self.inputs.append(int(input_1))
        return input_1

    """Функция, ставящая крестик или нолик на доске"""
    def make_point(self, coord, what):
        coord = int(coord)
        self.board[coord] = what
        return self.board

    def get_input(self, xo):
        input1 = input(f"Куда поставть {xo}?: ")
        while input1.isdigit() is False or int(input1) in self.inputs \
                or int(input1) > self.BOARD_SIZE ** 2:

            if input1.isdigit() is False:
                print("Вы ввели не число")

            if input1.isdigit() is True and int(input1) in self.inputs:
                print("Точка уже занята")

            if input1.isdigit() is True and int(input1) > 9:
                print("Введите число от 0 до 9")

            input1 = input(f"Куда поставть {xo}?: ")

        return input1

    def make_matrix(self):
        matrix = np.zeros((3, 3))
        count = 1

        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if self.board[count] == "X":
                    matrix[row][column] = 11
                elif self.board[count] == "O":
                    matrix[row][column] = 22
                else:
                    matrix[row][column] = self.board[count]
                count += 1
        return matrix

    """Функция, проверяющая, выиграл ли один из пользователей"""
    def check_winner(self):
        """Функция проверки победы"""
        matrix = self.make_matrix()
        for column in range(self.BOARD_SIZE):
            if matrix[column][0] == matrix[column][1] and matrix[column][1] == matrix[column][2]:
                return True
        for row in range(self.BOARD_SIZE):
            if matrix[0][row] == matrix[1][row] and matrix[1][row] == matrix[2][row]:
                return True

        if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
            return True
        if matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[0][2]:
            return True

    """Функция для старта игры"""
    def start_game(self):
        counter = 0
        self.show_board()
        x_or_o = "X"

        while self.check_winner() is not True:
            val = self.validate_input(self.get_input(x_or_o))
            self.make_point(val, x_or_o)
            self.show_board()
            if x_or_o == "X":
                x_or_o = "O"
            else:
                x_or_o = "X"

            if len(self.inputs) >= 9:
                break
            counter += 1

        if self.check_winner() is True:
            if x_or_o == "X":
                x_or_o = "O"
            else:
                x_or_o = "X"
            print(f"{x_or_o} победил!!!")
        else:
            x_or_o = "Draw"
            print("Ничья")

        return x_or_o


if __name__ == '__main__':
    print('Игра начинается!!!')
    game = TicTacGame()
    game.start_game()

