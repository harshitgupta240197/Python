import random

choice_list = ('r', 'p', 's')

def choice_of_user():
    while True:

        user_choice = input('Rock, Paper or Scissors (r/p/s) ?').lower()
        if user_choice in choice_list:
            return user_choice
        else:
            print('invalid choice')
            continue

def winning_logic(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('tie')
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        print('You won!')
    else:
        print('You lose!, try again!')

def playing_now():

    while True:

        computer_choice = random.choice(choice_list)

        user_choice = choice_of_user()

        winning_logic(user_choice, computer_choice)

        should_continue = input('Do you wish to continue ? (y/n): ').lower()

        if should_continue == 'n':
            break

playing_now()