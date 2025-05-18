def hangman_game():
    
    # Read inputs
    secret_word = input()
    # Slicing the string to remove "secret_word: " from input
    word = secret_word[13 : ]

    guesses = input()
    # Slicing the string to remove "guesses: " from input
    pure_guess = guesses[9 : ]
    

    # Convert secret_word into a list of characters
    revealed = [char if char in pure_guess else '_' for char in word]
    
    # Count incorrect guesses (unique guessed letters not in secret_word)
    incorrect_guesses = len(set(pure_guess) - set(word))
    
    # Format output as required
    print("Current state:", ' '.join(revealed))
    print("Incorrect guesses:", incorrect_guesses)

# Run the game
hangman_game()
