def display_board(board):
        
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def getBoardCopy(board):

     dupeBoard = []

     for i in board:

         dupeBoard.append(i)

     return dupeBoard          

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def chooseRandomMoveFromList(board, movesList):

     possibleMoves = []

     for i in movesList:

         if space_check(board, i):

             possibleMoves.append(i)

     if len(possibleMoves) != 0:

         return random.choice(possibleMoves)

     else:

         return None

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def computer_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = random.randint(1,9)
        
    return position        

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def getComputerMove(board, computerLetter):

     if computerLetter == 'X':

         playerLetter = 'O'

     else:

         playerLetter = 'X'

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if space_check(copy, i):

             place_marker(copy, computerLetter, i)

             if win_check(copy, computerLetter):

                 return i

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if space_check(copy, i):

             place_marker(copy, playerLetter, i)

             if win_check(copy, playerLetter):

                 return i

     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

     if move != None:

         return move

     if space_check(board, 5):

         return 5

     return chooseRandomMoveFromList(board, [2, 4, 6, 8])            

print('Welcome to Tic Tac Toe!')


while True:
    
    theBoard = [' '] * 10
    player1_marker, comp_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
               
            display_board(theBoard)
            position = getComputerMove(theBoard,comp_marker)
            place_marker(theBoard, comp_marker, position)

            if win_check(theBoard, comp_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break