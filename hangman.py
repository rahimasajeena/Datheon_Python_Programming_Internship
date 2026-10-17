import random

words = ["python", "computer", "program", "laptop", "student"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the hidden word, one letter at a time.")

while wrong_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

else:
    print("\nGame over! The word was:", word)

print("Thanks for playing!")