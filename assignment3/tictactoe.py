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

    def __str__(self):
        return (
            f" {self.board_array[0][0]} | "
            f"{self.board_array[0][1]} | "
            f"{self.board_array[0][2]} \n"
            "-----------\n"
            f" {self.board_array[1][0]} | "
            f"{self.board_array[1][1]} | "
            f"{self.board_array[1][2]} \n"
            "-----------\n"
            f" {self.board_array[2][0]} | "
            f"{self.board_array[2][1]} | "
            f"{self.board_array[2][2]} "
        )

    def move(self, move_string):
        move_string = move_string.lower().strip()

        if move_string not in self.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = self.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        winning_combinations = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],

            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],

            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        for combination in winning_combinations:
            first_row, first_column = combination[0]
            second_row, second_column = combination[1]
            third_row, third_column = combination[2]

            first_value = self.board_array[first_row][first_column]
            second_value = self.board_array[second_row][second_column]
            third_value = self.board_array[third_row][third_column]

            if (
                first_value != " "
                and first_value == second_value == third_value
            ):
                return True, f"{first_value} has won"

        # Check whether every board position is occupied
        board_is_full = all(
            space != " "
            for row in self.board_array
            for space in row
        )

        if board_is_full:
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

        move_string = input(f"{message}. Enter a move: ")

        try:
            board.move(move_string)
            print()
            print(board)

        except TictactoeException as error:
            print(error.message)
            print("Please try again.")