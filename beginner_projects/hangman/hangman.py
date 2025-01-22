import random
from word_list import words

selected_word = random.choice(words)
word_length = len(selected_word)
i = 0

while (i != word_length):
    print ("_", end=" ")
    i += 1


