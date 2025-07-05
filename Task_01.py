#Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
#Simplified Scope:
# Use a small list of 5 predefined words (no need to use a file or API)
# Limit incorrect guesses to 6.
# Basic console input/output no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.

import random

def hangman():
    """
    Plays a simple text-based Hangman game.
    """
    words = ["python", "hangman", "programming", "computer", "developer"]
    chosen_word = random.choice(words).lower()
    word_display = ["_" for _ in chosen_word]
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(chosen_word)} letters.")

    while incorrect_guesses < max_incorrect_guesses and "_" in word_display:
        print("\n" + " ".join(word_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    if "_" not in word_display:
        print("\n" + " ".join(word_display))
        print(f"\nCongratulations! You guessed the word: '{chosen_word}'")
    else:
        print("\n" + " ".join(word_display))
        print(f"\nGame over! You ran out of guesses. The word was: '{chosen_word}'")

if __name__ == "__main__":
    hangman()
