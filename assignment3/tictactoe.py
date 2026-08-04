# Task 6: More on Classes


# Custom exception
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Tic-tac-toe board
class Board:
    valid_moves = [
        "upper left",
        "upper center",
        "upper right",
        "middle left",
        "center",
        "middle right",
        "lower left",
        "lower center",
        "lower right",
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []
        lines.append(
            f" {self.board_array[0][0]} | "
            f"{self.board_array[0][1]} | "
            f"{self.board_array[0][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[1][0]} | "
            f"{self.board_array[1][1]} | "
            f"{self.board_array[1][2]} \n"
        )
        lines.append("-----------\n")
        lines.append(
            f" {self.board_array[2][0]} | "
            f"{self.board_array[2][1]} | "
            f"{self.board_array[2][2]} \n"
        )
        return "".join(lines)

    def move(self, move_string):
        move_string = move_string.lower().strip()

        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn
        self.last_move = (row, column)

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        win = False

        # Check rows
        for i in range(3):
            if (
                self.board_array[i][0] != " "
                and self.board_array[i][0]
                == self.board_array[i][1]
                == self.board_array[i][2]
            ):
                win = True
                break

        # Check columns
        if not win:
            for i in range(3):
                if (
                    self.board_array[0][i] != " "
                    and self.board_array[0][i]
                    == self.board_array[1][i]
                    == self.board_array[2][i]
                ):
                    win = True
                    break

        # Check diagonals
        if not win:
            if (
                self.board_array[0][0] != " "
                and self.board_array[0][0]
                == self.board_array[1][1]
                == self.board_array[2][2]
            ):
                win = True

            elif (
                self.board_array[0][2] != " "
                and self.board_array[0][2]
                == self.board_array[1][1]
                == self.board_array[2][0]
            ):
                win = True

        if win:
            if self.turn == "O":
                return True, "X has won"
            else:
                return True, "O has won"

        # Check whether the board is full
        cat = True

        for row in self.board_array:
            for space in row:
                if space == " ":
                    cat = False
                    break

            if not cat:
                break

        if cat:
            return True, "Cat's Game"

        return False, f"{self.turn}'s turn"


# Main program
if __name__ == "__main__":
    board = Board()
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("Valid moves:")
    print(", ".join(Board.valid_moves))
    print()
    print(board)

    while not game_over:
        game_over, message = board.whats_next()

        if game_over:
            print(message)
            break

        move_string = input(f"{message} Enter a move: ")

        try:
            board.move(move_string)
            print()
            print(board)

        except TictactoeException as error:
            print(error.message)
            print("Please try again.")

    game_over, message = board.whats_next()
    print(message)