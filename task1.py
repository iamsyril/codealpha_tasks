import random
def hangman():
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "software"]
    word = random.choice(words)
    max_attempts = 6
    incorrect_guesses = 0
    guessed_letters = set()
    current_word = ["_"] * len(word)
    print("Welcome to Hangman!")
    print(" ".join(current_word))
    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    current_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
        print(" ".join(current_word))
        if "_" not in current_word:
            print("Congratulations! You've guessed the word:", word)
            break
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    if incorrect_guesses == max_attempts:
        print("You've run out of attempts. The word was:", word)
hangman()
