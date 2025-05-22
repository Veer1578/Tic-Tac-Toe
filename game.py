# Implementation of 2 player Tic-Tac-Toe game in Python
'''We will make the board using dictionary in which keys will  be the location i.e top-left, mid'right etc. and initially it's value will be empty and then after every move we will, change the value according to player's choice of move.'''

Board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}
board_keys = []

for key in Board:
    board_keys.append(key)

'''We will have to print the updated board after every move in the game and thus we will make a function in which we will define the printBoard function so that we can easily print the board everytime by calling this function.'''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll  write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(Board)
        print(f"It's your turn, {turn}. Move to which place?")
        move = input()

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print('That place is already chosen.\nMove to which place?')
            continue

        #Now we will check which player has won every move after 5.
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':
                printBoard(Board)
                print('Game Over')
                print(f'**** {turn} won ****')
                break
        #If neither X nor O wins and board is full it will be tie.
        if count == 9:
            print('Game Over')
            print("Its's a tie")
        #We have to change player after every move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input('Do you want to play again(y/n)?: ')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            Board[key] = ' '

        game()
if __name__ == '__main__':
    game()    