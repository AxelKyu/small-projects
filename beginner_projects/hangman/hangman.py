import random
from word_list import words

def difficulty(word_length):
    options = {'1': 'easy', '2': 'normal', '3': 'hard'}
    level_input = input("Choose a Difficulty \n1. Easy \n2. Normal \n3. Hard \n: ")
    
    while level_input not in options:
        level_input = input("Invalid choice. Choose a Difficulty \n1. Easy \n2. Normal \n3. Hard: ")
    
    level = options[level_input]
    
    if level == "easy":
        guesses = word_length + 2
    elif level == "normal":
        guesses = word_length
    else:  # level == "hard"
        guesses = word_length - 2
    
    return guesses

def display_word(selected_word, guessed_letters):
    display = [letter if letter in guessed_letters else "_" for letter in selected_word]
    return " ".join(display)

# Game Initialization
if not words:
    print("The word list is empty. Please provide words to play the game.")
    exit()

selected_word = random.choice(words).lower()
word_length = len(selected_word)

# Display Of Word Length
print("Word to guess: " + " ".join(["_"] * word_length))

# Set Guesses Based on Difficulty
guesses = difficulty(word_length)
print(f"Number of guesses allowed: {guesses}")

# Initialize Game Variables
guessed_letters = set()
remaining_guesses = guesses

# Game Loop
while remaining_guesses > 0:
    print("\n" + display_word(selected_word, guessed_letters))
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    elif guess not in selected_word:
        remaining_guesses -= 1
        print(f"Incorrect! Guesses remaining: {remaining_guesses}")
    else:
        print("Good guess!")
    
    guessed_letters.add(guess)
    
    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in selected_word):
        print(f"\nCongratulations! You've guessed the word: {selected_word}")
        break
else:
    print(f"\nSorry, you've run out of guesses. The word was: {selected_word}")
