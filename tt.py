import random

# Word list for the game
words = ["python", "computer", "hangman", "developer", "notebook", "keyboard", "internet"]

# Choose a random word
chosen_word = random.choice(words)
word_display = ["_"] * len(chosen_word)
attempts = 6
guessed_letters = []

print("🎯 Welcome to Hangman!")
print("Guess the word:")

while attempts > 0:
    print("\nWord:", " ".join(word_display))
    print(f"Attempts left: {attempts}")
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Enter only one letter (a-z)!")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter, try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✔ Good guess!")

        for i, char in enumerate(chosen_word):
            if char == guess:
                word_display[i] = guess
    else:
        print("❌ Wrong guess!")
        attempts -= 1

    if "_" not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", chosen_word)
        break

if attempts == 0:
    print("\n💀 Game Over! The word was:", chosen_word)
