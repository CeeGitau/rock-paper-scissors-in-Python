import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors'] #this is a list of elements

name = input('Enter your name: ')
print('Welcome to my game', name +'!')

while True:
    user_input = input('Type rock/paper/scissors or Q to quit: ').lower()
    if user_input == 'q':
        break #stops the loop in which the statementis placed

    if user_input not in options:
        continue #skips a single iteration in a loop

    random_number = random.randint(0, 2)
    # rock: 0, paper:1, scissors:2
    #elements in a list are usually indexed from zero (0)

    computer_pick = options[random_number]
    print('Computer picked', computer_pick)

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You won! :)')
        user_wins += 1
    
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You won! :)')
        user_wins += 1
     
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You won! :)')
        user_wins += 1

    elif user_input == computer_pick:
        print('It was a tie')
        
    else:
        print('You lost! :(')
        computer_wins += 1

print('You won', user_wins, 'times.')
print('The computer won', computer_wins, 'times.')
print('Thank you for playing ^-^')
print('Goodbye')
