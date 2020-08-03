import random

# This function will run the game until closed
def RPSGame():
    userCount, myCount = 0, 0
    roundCount = 1
    while True:
        print('*'*10, f'Rount {roundCount}', '*'*10)
        userGuess = input('Enter Rock, Paper, or Scissors or Q to Quit: ')
        myGuess = random.choice(['Rock', 'Paper', 'Scissors'])
        # If-elif statements to check who won each round and to increment the score counters
        if userGuess == 'Q':
            print('Quitting........\n')
            break
        elif userGuess == 'Rock':
            if myGuess == 'Paper':
                myCount += 1
                print('I Win\n')
            elif myGuess == 'Scissors':
                userCount += 1
                print('You Win\n')
            else:
                print('No One Wins. Onto the Next Round\n')
        elif userGuess == 'Paper':
            if myGuess == 'Scissors':
                myCount += 1
                print('I Win\n')
            elif myGuess == 'Rock':
                userCount += 1 
                print('You Win\n')
            else:
                print('No One Wins. Onto the Next Round\n')
        elif userGuess == 'Scissors':
            if myGuess == 'Rock':
                myCount += 1
                print('I Win\n')
            elif myGuess == 'Paper':
                userCount += 1 
                print('You Win\n')
            else:
                print('No One Wins. Onto the Next Round\n')
        else:
            print('Invalid Input...Try Again\n')
        roundCount += 1
    # This function returns both the player and the computer score
    return userCount, myCount

# This fucntion uses the scores returned from the RPSGame() function and decides the winner
def endGame(playerScore, computerScore):
    if playerScore == computerScore:
        print(f'It\'s a Tie ({playerScore}-{computerScore})')
    elif playerScore > computerScore:
        print(f'You Win ({playerScore}-{computerScore})')
    elif playerScore < computerScore:
        print(f'I Win ({computerScore}-{playerScore})')
  
# Tuple unpacking into variables p and c
p, c, = RPSGame()  
endGame(p, c)
