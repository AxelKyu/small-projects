import random
from word_list import words

#Game Difficuly Menu

def difficulty(word_length, lives):
    option = ['easy', 'normal', 'hard']
    level = input ("Choose a Difficulty \n1. Easy \n2. Normal \n3. Hard").lower()
    
    while (level not in option):
            level = input ("Invalid Difficulty. Choose a Difficulty \n1. Easy \n2. Normal \n3. Hard").lower()

    if (level == "easy"):
        lives = word_length + 2
    elif (level == "Normal"):
        lives = word_length
    else:
        lives = word_length - 2

# Game Initialization
selected_word = random.choice(words)
word_length = len(selected_word)
i = 0
lives = 0

# Display Of Word Length
while (i != word_length):
    print ("_", end=" ")
    i += 1


difficulty(word_length, lives)