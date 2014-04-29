SIZE = 3

def wincheck(board, player):
    win_check = False

    # vertical checks
    for a in range(SIZE):
        for b in range(SIZE):
            if(board[a+(b*SIZE)] != player):
                win_check = False
                break
            else: win_check = True
        if(win_check): return 'win'

    # horizontal checks
    for a in range(SIZE):
        for b in range(SIZE):
            if(board[b+(a*SIZE)] != player):
                win_check = False
                break
            else: win_check = True
        if(win_check): return 'win'

    # diagonal checks, first top left to bottom right
    for a in range(SIZE):
        if(board[a*(SIZE+1)] != player):
            win_check = False
            break
        else: win_check = True
    if(win_check): return 'win'

    # now top right to bottom left
    for a in range(SIZE):
        if(board[(a+1)*(SIZE-1)] != player):
            win_check = False
            break
        else: win_check = True
    if(win_check): return 'win'

    # checking for tie, has to be at end because need to garentee no wins
    if(' ' not in board):
        return 'tie'

    # no wins or ties
    return 'nowin'

def print_board(board):
    for y in range(SIZE):
        print('')
        print('-' * ((SIZE * 2) + 1))
        print('|', end = '')
        for x in range(SIZE):
            print(board[(y*SIZE) + x], end = '|')
    print('')
    print('-' * ((SIZE * 2) + 1))

def turn(board, player):
    location = -1
    while(True):
        print('PLAYER ' + player + "'s TURN")
        print('Position numbers increase left to right')
        print('then top to bottom, starting at 1.')
        userinput = input('\nEnter the position: ')
        try:
            location = int(userinput)
        except ValueError:
            print('Error in input, input was not an integer, please try again')
            print_board(board)
        else:
            location -= 1
            if (location >= 0 and location < len(board)
                and board[location] == ' '):
                break
            else:
                print('Error in input, not a valid position, please try again')
                print_board(board)
    board[location] = player

def play():
    board = [" "] * (SIZE * SIZE)

    playerturn = True ## True is player 1, False is player 2
    while(True):
        print_board(board)
        if(playerturn): player = 'X'
        else: player = 'O'

        turn(board, player)
        result = wincheck(board, player)
        if(result == 'win'):
            print_board(board)
            print('X wins!' if playerturn else 'O wins!')
            break
        elif(result == 'tie'):
            print_board(board)
            print('Both players tie! Cats Game!')
            break
        playerturn = not playerturn

if __name__ == '__main__':
    game = True
    while(game):
        print('Type 1 to exit\nType 2 to play TicTacToe')
        answer = str(input('> '))
        if(answer == '1'):
            game = False
        elif(answer == '2'):
            play()
            break