# Task 4: Closure Practice

#declare make_hangman
def make_hangman(secret_word):
   guesses=[]

   def hangman_closure(letter):
    guesses.append(letter)
    display_word=""

    for char in secret_word:
        if char in guesses:
           display_word+=char
        else:
           display_word+="_"

    print(display_word)
    return "_" not in display_word
   return hangman_closure

#main program
if __name__=="__main__":
   secret_word=input("Enter the secret word: ")

   game=make_hangman(secret_word)

   solved=False
   while not solved:
      guess=input("Guess a letter: ")
      solved=game(guess)

print("Congratulations! You guessed the word!")
   