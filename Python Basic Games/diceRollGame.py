# Loop 
    # Ask the user to roll a dice ?
    # If user enters y thebb 
    # Generate random numbers
    # Print the random numbers
    # If the user enter n
    # Print thank you message
    # Terminate the program
    # If the users enters anything else then print 'invalid choice'

import random

counter = 0

while True:

    user_input = input('Do you want to roll the dice ?').lower()
    
    if user_input == 'y':
        user_input_2 = int(input('Specify how many times you want to roll the dice ?'))
        for i in range(user_input_2):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f'{dice1}, {dice2}')
        counter = counter + user_input_2
    elif user_input == 'n':
        print(f'thank you, you rolled the dice {counter} times!')
        break
    else:
        print('Invalid input')




