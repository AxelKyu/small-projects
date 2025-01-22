import random 

def game():
    choice = ['rock', 'paper', 'scissors']
    user_input = input("Enter Rock, Paper or Scissors: ").lower()

    while user_input not in choice:
        user_input = input("Invalid input. Enter Rock, Paper or Scissors: ").lower()

    computer_choice = random.choice(choice)

    if computer_choice == user_input:
        print(f"Your Choice: {user_input} \nComputer's Choice: {computer_choice}")
        print("It's a Tie!")
    elif (computer_choice == "paper" and user_input == "rock") or \
         (computer_choice == "rock" and user_input == "scissors") or \
         (computer_choice == "scissors" and user_input == "paper"):
        print(f"Your Choice: {user_input} \nComputer's Choice: {computer_choice}")
        print("Computer Wins!")
    else:
        print(f"Your Choice: {user_input} \nComputer's Choice: {computer_choice}")
        print("You Win!")

game()
