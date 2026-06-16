import random

words = ["apple", "mango", "table", "tiger", "water"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)