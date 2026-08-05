# Task 4: Closure Practice

# Declare make_hangman
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""

        for char in secret_word:
            if char in guesses:
                display_word += char
            else:
                display_word += "_"

        print(display_word)

        # Return True only if every letter has been guessed
        return all(char in guesses for char in secret_word)

    return hangman_closure


# Main program
if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")

    game = make_hangman(secret_word)

    solved = False
    while not solved:
        guess = input("Guess a letter: ")
        solved = game(guess)

    print("Congratulations! You guessed the word!")