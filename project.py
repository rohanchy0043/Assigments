import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    word_to_guess = random.choice(words)
    guessed_word = ["_" for _ in word_to_guess]
    attempts_left = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while attempts_left > 0:
        print("\nWord to guess:", " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess

            if "_" not in guessed_word:
                print("\nCongratulations! You've guessed the word:", word_to_guess)
                break
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1

    if attempts_left == 0:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
