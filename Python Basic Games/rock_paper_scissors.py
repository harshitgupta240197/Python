# Game that has options for the user to select from r/p/s = rock/paper/scissors
# throw invalid choice error incase the user enters anything outside r/p/s
# write decisions/logic for rock, paper and scissors

import random

choice_list = ('r', 'p', 's')

while True:

    computer_choice = random.choice(choice_list)

    user_choice = input('Rock, Paper or Scissors (r/p/s) ?').lower()

    if user_choice not in choice_list:
        print('invalid choice')
        continue
    if user_choice == computer_choice:
        print('tie')
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 's' and computer_choice == 'p') or \
         (user_choice == 'p' and computer_choice == 'r'):
        print('You won!')
    else:
        print('You lose!, try again!')

    should_continue = input('Do you wish to continue ? (y/n): ').lower()

    if should_continue == 'n':
        break

    


