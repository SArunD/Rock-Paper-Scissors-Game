# Here, we import the Random Module
import random

# Here, we define the global variables for our RPS Game
player_wins, computer_wins = (0, 0)
is_quit = False


# This function starts our RPS Game
def start_game():
    global player_wins, computer_wins, is_quit
    # This variable stores what round we're playing in
    current_round = 1
    # This loop will run until is_quit is True
    while not is_quit:
        # At each iteration, print the round #, obtain user-input, and increment round counter
        print(('*' * 11 + ' Round #{} ' + '*' * 11).format(current_round))
        get_input_print()
        current_round += 1

    # Here, we ask the user if they want to try again
    retry = input('\nTry Again? (Yes or No) ')
    print()
    # If user enters yes, then call start_game() and reset global variables
    if retry == 'Yes':
        player_wins, computer_wins = (0, 0)
        is_quit = False
        start_game()
    # If user enters no, then END
    else:
        print('Thank You For Playing!!!')


# This function gets both moves and sends them to check_moves_wins()
def get_input_print():
    # Here, we get the move from Player and pick a random move for Computer
    player_move = input('Options:\n\tR - Rock\n\tP - Paper\n\tS - Scissors\n\tQ - Quit\n'
                        'Choose Your Move: ')
    computer_move = random.choice(['R', 'P', 'S'])

    # If Player move is not Quit, then print each move
    moves = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    if player_move != 'Q':
        print('\nYou Picked:\t\t\t[{}]'
              '\nComputer Picked:\t[{}]'.format(moves.get(player_move), moves.get(computer_move)))

    # Then, call check_moves_wins() by passing both moves as parameters
    check_moves_wins(player_move, computer_move)


# This function checks each move and adds points accordingly
def check_moves_wins(player_move, computer_move):
    # We're specifically going to modify global point (or win) trackers
    global player_wins, computer_wins, is_quit
    # This is a basic template for displaying who wins the current round
    template = '\n{} Win{} This Round!\n'

    # This nested conditional check all possibles moves and add points
    if player_move == 'R':
        if computer_move == 'P':
            # If Computer wins, then add 1 point to Computer and print that out
            computer_wins += 1
            print(template.format('Computer', 's'))
        elif computer_move == 'S':
            # If Player wins, then add 1 point to Player and print that out
            player_wins += 1
            print(template.format('You', ''))
        else:
            # If No One Wins, then print that out
            print('\nNo One Wins! Draw!\n')
    elif player_move == 'P':
        if computer_move == 'S':
            computer_wins += 1
            print(template.format('Computer', 's'))
        elif computer_move == 'R':
            player_wins += 1
            print(template.format('You', ''))
        else:
            print('\nNo One Wins! Draw!\n')
    elif player_move == 'S':
        if computer_move == 'R':
            computer_wins += 1
            print(template.format('Computer', 's'))
        elif computer_move == 'P':
            player_wins += 1
            print(template.format('You', ''))
        else:
            print('\nNo One Wins! Draw!\n')
    # If Player move is Quit, then set is_quit to False and call end_game()
    elif player_move == 'Q':
        end_game()
        is_quit = True


# This function ends our RPS Game and prints out each candidate's points
def end_game():
    print('\n' + ('*' * 13 + ' QUIT ' + '*' * 13).format(round))
    print('\n' + ('*' * 12 + ' RESULT ' + '*' * 12).format(round))
    print('\nYour Score:\t\t[{}]\nComputer Score:\t[{}]'.format(player_wins, computer_wins))

    # If Player has more points, Player wins
    if player_wins > computer_wins:
        print('\nCongrats! You Won The Game!')
    # If Computer has more points, Computer wins
    elif player_wins < computer_wins:
        print('\nOh! The Computer Won The Game!')
    # If both have same # of points, no one wins
    else:
        print('\nNo One Wins! It\'s a Draw!')

    print('\n' + ('*' * 32))


# Here, we start our RPS Game by calling start_game()
start_game()
