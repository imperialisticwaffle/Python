# We are going to store a secret word; the user will have to keep guessing until the secret word is matched.
secret_word = "Giraffe"
guess = "" # We are keeping a variable for their guesses
# Now, we need a while loop.
while guess != secret_word:
    guess = str(raw_input("Guess the secret word: ")) 
    if guess != secret_word:
        print("Wrong word! Guess again. :)")
print("Congratulations! You guessed the secret word.")

# This is a fairly basic guessing game. Perhaps we can make it more complex by adding a max # of guesses.
secret_word = "Giraffe"
guess = ""
guess_count = 0
while guess != secret_word:
    guess = str(raw_input("Guess the secret word: ")) 
    if guess != secret_word:
        print("Wrong word! Guess again. :)")
        guess_count = guess_count + 1
    if guess_count == 3:
        print("Oh no! You've reached the max number of guesses. Try again later :(")
print("Congratulations! You guessed the secret word.")

# Trying with a different approach...
secret_word = "Giraffe"
guess = ""
guess_count = 0
max_guesses = 2
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    guess = str(raw_input("Guess the secret word: ")) 
    if guess_count < max_guesses:
        print("Wrong word! Guess again. :)")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True
if out_of_guesses == True:
    print("Oh no! You've reached the max number of guesses. Try again later :(")
else:
    print("Congratulations! You guessed the secret word.")