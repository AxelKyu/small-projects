import random 

low = int(input("Low: "))
high = int(input("High: ")) 

def computer_guess(low, high):

    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is the guess {guess} \nHigh (H), Low (L)) or Correct (C): ").lower()

        if (feedback == 'h'):
            high = guess - 1
        elif (feedback == 'l'):
            low = low + 1
    
    print(f"Correct Number is {guess}")


computer_guess(low, high)