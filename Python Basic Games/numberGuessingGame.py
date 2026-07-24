# Guess the number 1 and 100
# Show a invalid number message if entered number is invalid
# If the guessed number is too high then display too high
# If the guessed number is tooo low then display too low
# Say Congrats if the guessed number matches

import random

real_number = random.randint(1, 100)

while True:

    try: 
        user_input = int(input('Guess the number between 1 and 100: '))
    except ValueError:
        print('Please enter a valid number')
        continue

    if user_input > real_number:
        print('The number is too High!')
    elif user_input < real_number:
        print('The number is too low!')
    elif user_input == real_number:
        print('Congratulations you guessed right!')
        break