

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

def get_valid_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_valid_moves():
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_valid_moves():
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    best_move = None
    for move in get_valid_moves():
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    make_move('O', best_move)

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while ' ' in board:
        position = int(input("Enter your move (1-9): ")) - 1
        if position not in get_valid_moves():
            print("Invalid move, try again.")
            continue

        make_move('X', position)
        print_board()

        if check_winner('X'):
            print("Congratulations! You win!")
            break

        if ' ' not in board:
            print("It's a draw!")
            break

        ai_move()
        print("AI has made a move:")
        print_board()

        if check_winner('O'):
            print("AI wins! Better luck next time.")
            break

    else:
        print("It's a draw!")


board = [' ' for _ in range(9)]
play_game()
