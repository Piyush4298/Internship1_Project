board = {
    'p1': ' ', 'p2': ' ', 'p3': ' ',
    'p4': ' ', 'p5': ' ', 'p6': ' ',
    'p7': ' ', 'p8': ' ', 'p9': ' '
}
# p is position of element
print('p1 | p2 | p3')
print('---+----+---')
print('p4 | p5 | p6')
print('---+---+---')
print('p7 | p8 | p9\n')
print('Enter the respective position chance by chance!\n', 'Player 1 : X and Player 2 : O')
total_moves = 0
player = 1
end_check = 0


def check():
    if board['p1'] == board['p2'] == board['p3'] == 'X':
        return 1, 'Player one won !'
    elif board['p4'] == board['p5'] == board['p6'] == 'X':
        return 1, 'Player one won !'
    elif board['p7'] == board['p8'] == board['p9'] == 'X':
        return 1, 'Player one won !'
    elif board['p1'] == board['p5'] == board['p9'] == 'X':
        return 1, 'Player one won !'
    elif board['p1'] == board['p4'] == board['p7'] == 'X':
        return 1, 'Player one won !'
    elif board['p2'] == board['p5'] == board['p8'] == 'X':
        return 1, 'Player one won !'
    elif board['p3'] == board['p6'] == board['p9'] == 'X':
        return 1, 'Player one won !'
    elif board['p1'] == board['p2'] == board['p3'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p4'] == board['p5'] == board['p6'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p7'] == board['p8'] == board['p9'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p1'] == board['p5'] == board['p9'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p1'] == board['p4'] == board['p7'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p2'] == board['p5'] == board['p8'] == 'O':
        return 1, 'Player Two Won!!'
    elif board['p3'] == board['p6'] == board['p9'] == 'O':
        return 1, 'Player Two Won!!'
    else:
        return 0, "No one won, It is a Draw!!!!"


while True:
    print(board['p1'] + ' | ' + board['p2'] + ' | ' + board['p3'])
    print('--+---+---')
    print(board['p4'] + ' | ' + board['p5'] + ' | ' + board['p6'])
    print('--+---+---')
    print(board['p7'] + ' | ' + board['p8'] + ' | ' + board['p9'])
    end_check, string = check()
    if total_moves == 9 or end_check == 1:
        print(string)
        break
    elif end_check == 0 and total_moves == 9:
        print(string)
        break
    while True:
        if player == 1:
            player_1_input = input('Player one(X): ')
            if player_1_input in board and board[player_1_input] == ' ':
                board[player_1_input] = 'X'
                player = 2
                break
            else:
                print("Invalid input , choose one from board displayed ,or check if already marked :-)")
                continue
        else:
            player_2_input = input('Player two(O): ')
            if player_2_input in board and board[player_2_input] == ' ':
                board[player_2_input] = 'O'
                player = 1
                break
            else:
                print("Invalid input , choose one from board displayed ,or check if already marked :-)")

    total_moves += 1
